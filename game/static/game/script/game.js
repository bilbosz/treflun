"use strict";

var app = {
    tokenDragHandler: null,
    serverCommunication: null
};

var utils = {
    translateMouseToSvg: function( svg, x, y )
    {
        var point = svg.createSVGPoint();
        point.x = x;
        point.y = y;
        return point.matrixTransform( svg.getCTM().inverse() );
    },

    findClassStartWith: function( classList, startsWith )
    {
        for( var i = 0; i < classList.length; ++i )
        {
            if( classList[i].startsWith( startsWith ) ) {
                return classList[i];
            }
        }
        return null;
    }
}

function TokenDragHandler() {
    var self = this;

    self.reset = function() {
        self.down = false;
        self.tokens = null;
        self.token = null;
        self.offsetX = null;
        self.offsetY = null;
    };
    self.reset();

    var svg = document.getElementsByTagName( "svg" )[0];

    svg.addEventListener( "mousedown", function( e ) {
        var icon = e.target;
        if( icon.classList.contains( "token-icon" ) )
        {
            self.down = true;
            var tokenId = utils.findClassStartWith( icon.parentNode.classList, "token-id-" );
            self.tokens = svg.getElementsByClassName( tokenId );
            self.token = self.tokens[0];

            var tokenX = parseFloat( self.token.getAttribute( "data-x" ) );
            var tokenY = parseFloat( self.token.getAttribute( "data-y" ) );
            var point = utils.translateMouseToSvg( svg, e.offsetX, e.offsetY );

            self.offsetX = tokenX - point.x;
            self.offsetY = tokenY - point.y;
        }
    } );
    svg.addEventListener( "mousemove", function( e ) {
        if( self.down )
        {
            var point = utils.translateMouseToSvg( svg, e.offsetX, e.offsetY );
            point.x = point.x + self.offsetX;
            point.y = point.y + self.offsetY;

            for( var i = 0; i < self.tokens.length; ++i )
            {
                var token = self.tokens[i];
                token.setAttribute( "data-x", point.x );
                token.setAttribute( "data-y", point.y );
                token.setAttribute( "transform", "translate(" + point.x + ", " + point.y + ")" );
            }
        }
    } );
    svg.addEventListener( "mouseup", function( e ) {
        if( self.down )
        {
            app.serverCommunication.SetTokenPosition( self.token.getAttribute( "data-token-id" ), self.token.getAttribute( "data-x" ), self.token.getAttribute( "data-y" ) );
        }
        self.reset();
    } );
}

function ServerCommunication()
{
    var self = this;

    self.reset = function() {
        self.connection = new WebSocket( "ws://" + window.location.host + "/ws/game/1/" );
    };
    self.reset();

    self.connection.onmessage = function( e ) {
        const data = JSON.parse( e.data );
        var tokens = document.getElementsByClassName( "token-id-" + parseInt( data.id ) );
        for( var i = 0; i < tokens.length; ++i )
        {
            var token = tokens[i];
            token.setAttribute( "data-x", data.x );
            token.setAttribute( "data-y", data.y );
            token.setAttribute( "transform", "translate(" + data.x + ", " + data.y + ")" );
        }
    };

    self.connection.onclose = function( e ) {
    };

    self.SetTokenPosition = function( id, x, y ) {
        self.connection.send( JSON.stringify( {
            "id": id,
            "x": x,
            "y": y
        } ) );
    };
}

document.addEventListener( "DOMContentLoaded", function() {
    app.tokenDragHandler = new TokenDragHandler();
    app.serverCommunication = new ServerCommunication();
} );