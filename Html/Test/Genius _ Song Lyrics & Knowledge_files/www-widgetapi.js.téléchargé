(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var p;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var da="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ea(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var fa=ea(this);function t(a,b){if(b)a:{var c=fa;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&da(c,a,{configurable:!0,writable:!0,value:b})}}
t("Symbol",function(a){function b(f){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(f||"")+"_"+e++,f)}
function c(f,g){this.h=f;da(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",e=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=fa[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&da(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ha(aa(this))}})}return a});
function ha(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function ia(a){if(!(a instanceof Array)){a=u(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
function ja(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var ka="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)ja(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||ka});
var la="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ma;
if("function"==typeof Object.setPrototypeOf)ma=Object.setPrototypeOf;else{var na;a:{var oa={a:!0},pa={};try{pa.__proto__=oa;na=pa.a;break a}catch(a){}na=!1}ma=na?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var qa=ma;
function v(a,b){a.prototype=la(b.prototype);a.prototype.constructor=a;if(qa)qa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.O=b.prototype}
function sa(){this.u=!1;this.l=null;this.i=void 0;this.h=1;this.o=this.m=0;this.G=this.j=null}
function ta(a){if(a.u)throw new TypeError("Generator is already running");a.u=!0}
sa.prototype.C=function(a){this.i=a};
function va(a,b){a.j={Ta:b,Za:!0};a.h=a.m||a.o}
sa.prototype.return=function(a){this.j={return:a};this.h=this.o};
function w(a,b,c){a.h=c;return{value:b}}
sa.prototype.s=function(a){this.h=a};
function wa(a,b,c){a.m=b;void 0!=c&&(a.o=c)}
function xa(a,b){a.h=b;a.m=0}
function ya(a){a.m=0;var b=a.j.Ta;a.j=null;return b}
function za(a){a.G=[a.j];a.m=0;a.o=0}
function Ba(a){var b=a.G.splice(0)[0];(b=a.j=a.j||b)?b.Za?a.h=a.m||a.o:void 0!=b.s&&a.o<b.s?(a.h=b.s,a.j=null):a.h=a.o:a.h=0}
function Ca(a){this.h=new sa;this.i=a}
function Da(a,b){ta(a.h);var c=a.h.l;if(c)return Ea(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Fa(a)}
function Ea(a,b,c,d){try{var e=b.call(a.h.l,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.u=!1,e;var f=e.value}catch(g){return a.h.l=null,va(a.h,g),Fa(a)}a.h.l=null;d.call(a.h,f);return Fa(a)}
function Fa(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.u=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,va(a.h,c)}a.h.u=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.Za)throw b.Ta;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ga(a){this.next=function(b){ta(a.h);a.h.l?b=Ea(a,a.h.l.next,b,a.h.C):(a.h.C(b),b=Fa(a));return b};
this.throw=function(b){ta(a.h);a.h.l?b=Ea(a,a.h.l["throw"],b,a.h.C):(va(a.h,b),b=Fa(a));return b};
this.return=function(b){return Da(a,b)};
this[Symbol.iterator]=function(){return this}}
function Ha(a){function b(d){return a.next(d)}
function c(d){return a.throw(d)}
return new Promise(function(d,e){function f(g){g.done?d(g.value):Promise.resolve(g.value).then(b,c).then(f,e)}
f(a.next())})}
function x(a){return Ha(new Ga(new Ca(a)))}
function Ia(){for(var a=Number(this),b=[],c=a;c<arguments.length;c++)b[c-a]=arguments[c];return b}
t("Reflect.setPrototypeOf",function(a){return a?a:qa?function(b,c){try{return qa(b,c),!0}catch(d){return!1}}:null});
t("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.u=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.o()})}this.h.push(g)};
var e=fa.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.o=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(m){k||(k=!0,l.call(h,m))}}
var h=this,k=!1;return{resolve:g(this.Ha),reject:g(this.o)}};
b.prototype.Ha=function(g){if(g===this)this.o(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.jb(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.Ga(g):this.m(g)}};
b.prototype.Ga=function(g){var h=void 0;try{h=g.then}catch(k){this.o(k);return}"function"==typeof h?this.kb(h,g):this.m(g)};
b.prototype.o=function(g){this.C(2,g)};
b.prototype.m=function(g){this.C(1,g)};
b.prototype.C=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.Ia();this.G()};
b.prototype.Ia=function(){var g=this;e(function(){if(g.V()){var h=fa.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.V=function(){if(this.u)return!1;var g=fa.CustomEvent,h=fa.Event,k=fa.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=fa.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.G=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.jb=function(g){var h=this.l();g.va(h.resolve,h.reject)};
b.prototype.kb=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,q){return"function"==typeof r?function(y){try{l(r(y))}catch(A){m(A)}}:q}
var l,m,n=new b(function(r,q){l=r;m=q});
this.va(k(g,l),k(h,m));return n};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.va=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.u=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),m=l.next();!m.done;m=l.next())d(m.value).va(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,m){function n(y){return function(A){r[y]=A;q--;0==q&&l(r)}}
var r=[],q=0;do r.push(void 0),q++,d(k.value).va(n(r.length-1),m),k=h.next();while(!k.done)})};
return b});
t("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!ja(k,g)){var l=new c;da(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(m){if(m instanceof c)return m;Object.isExtensible(m)&&e(m);return l(m)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),m=new a([[k,2],[l,3]]);if(2!=m.get(k)||3!=m.get(l))return!1;m.delete(k);m.set(l,4);return!m.has(k)&&4==m.get(l)}catch(n){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!ja(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&ja(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&ja(k,g)&&ja(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&ja(k,g)&&ja(k[g],this.h)?delete k[g][this.h]:!1};
return b});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.h;return ha(function(){if(l){for(;l.head!=h.h;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var m=h.data_[l];if(m&&ja(h.data_,l))for(h=0;h<m.length;h++){var n=m[h];if(k!==k&&n.key!==n.key||k===n.key)return{id:l,list:m,index:h,entry:n}}return{id:l,list:m,index:-1,entry:void 0}}
function e(h){this.data_={};this.h=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),m=l.next();if(m.done||m.value[0]!=h||"s"!=m.value[1])return!1;m=l.next();return m.done||4!=m.value[0].x||"t"!=m.value[1]||!l.next().done?!1:!0}catch(n){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.data_[l.id]=[]);l.entry?l.entry.value=k:(l.entry={next:this.h,previous:this.h.previous,head:this.h,key:h,value:k},l.list.push(l.entry),this.h.previous.next=l.entry,this.h.previous=l.entry,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.entry&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.data_[h.id],h.entry.previous.next=h.entry.next,h.entry.next.previous=h.entry.previous,h.entry.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.data_={};this.h=this.h.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).entry};
e.prototype.get=function(h){return(h=d(this,h).entry)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),m;!(m=l.next()).done;)m=m.value,h.call(k,m[1],m[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
function Ja(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ja(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
t("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ja(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
t("Number.isFinite",function(a){return a?a:function(b){return"number"!==typeof b?!1:!isNaN(b)&&Infinity!==b&&-Infinity!==b}});
t("Number.isInteger",function(a){return a?a:function(b){return Number.isFinite(b)?b===Math.floor(b):!1}});
t("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
function Ka(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
t("Array.prototype.entries",function(a){return a?a:function(){return Ka(this,function(b,c){return[b,c]})}});
t("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};
var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
t("Array.prototype.keys",function(a){return a?a:function(){return Ka(this,function(b){return b})}});
t("Array.prototype.values",function(a){return a?a:function(){return Ka(this,function(b,c){return c})}});
t("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
t("Object.setPrototypeOf",function(a){return a||qa});
t("Set",function(a){function b(c){this.h=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)ja(b,d)&&c.push([d,b[d]]);return c}});
t("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
t("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ja(this,b,"includes").indexOf(b,c||0)}});
var z=this||self;function B(a,b,c){a=a.split(".");c=c||z;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function C(a,b){a=a.split(".");b=b||z;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function La(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Oa(a){var b=La(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Pa(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Qa(a){return Object.prototype.hasOwnProperty.call(a,Ra)&&a[Ra]||(a[Ra]=++Sa)}
var Ra="closure_uid_"+(1E9*Math.random()>>>0),Sa=0;function Ta(a,b,c){return a.call.apply(a.bind,arguments)}
function Ua(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function Va(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?Va=Ta:Va=Ua;return Va.apply(null,arguments)}
function D(a,b){function c(){}
c.prototype=b.prototype;a.O=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.dc=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function Wa(a){return a}
;function Xa(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,Xa);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)}
D(Xa,Error);Xa.prototype.name="CustomError";function Ya(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function Za(){}
function ab(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var bb=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},E=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},cb=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},db=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
E(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function eb(a,b){b=bb(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function fb(a){return Array.prototype.concat.apply([],arguments)}
function gb(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function hb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Oa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function ib(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function jb(a){var b=kb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function lb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function mb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();if("undefined"!==typeof Map&&a instanceof Map)return new Map(a);if("undefined"!==typeof Set&&a instanceof Set)return new Set(a);if(a instanceof Date)return new Date(a.getTime());var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=mb(a[c]);return b}
var nb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function ob(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<nb.length;f++)c=nb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var qb;function rb(){}
function sb(a){return new rb(tb,a)}
var tb={};sb("");var ub=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]},Ab=/&/g,Bb=/</g,Cb=/>/g,Db=/"/g,Eb=/'/g,Fb=/\x00/g,Gb=/[\x00&<>"']/;function Hb(a,b){this.h=b===Ib?a:""}
Hb.prototype.toString=function(){return this.h.toString()};
var Ib={},Jb=new Hb("about:invalid#zClosurez",Ib);function Kb(){var a=z.navigator;return a&&(a=a.userAgent)?a:""}
function F(a){return-1!=Kb().indexOf(a)}
;function Lb(){return(F("Chrome")||F("CriOS"))&&!F("Edge")||F("Silk")}
;var Mb={};function Nb(a){this.h=Mb===Mb?a:""}
Nb.prototype.toString=function(){return this.h.toString()};var Ob=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function Pb(a){return a?decodeURI(a):a}
function Qb(a){return Pb(a.match(Ob)[3]||null)}
function Rb(a){var b=a.match(Ob);a=b[1];var c=b[2],d=b[3];b=b[4];var e="";a&&(e+=a+":");d&&(e+="//",c&&(e+=c+"@"),e+=d,b&&(e+=":"+b));return e}
function Sb(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)Sb(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Tb(a){var b=[],c;for(c in a)Sb(c,a[c],b);return b.join("&")}
var Yb=/#|$/;function Zb(a,b){var c=a.search(Yb);a:{var d=0;for(var e=b.length;0<=(d=a.indexOf(b,d))&&d<c;){var f=a.charCodeAt(d-1);if(38==f||63==f)if(f=a.charCodeAt(d+e),!f||61==f||38==f||35==f)break a;d+=e+1}d=-1}if(0>d)return null;e=a.indexOf("&",d);if(0>e||e>c)e=c;d+=b.length+1;return decodeURIComponent(a.slice(d,-1!==e?e:0).replace(/\+/g," "))}
;function $b(a){z.setTimeout(function(){throw a;},0)}
;function ac(){return F("iPhone")&&!F("iPod")&&!F("iPad")}
;function bc(a){bc[" "](a);return a}
bc[" "]=function(){};var cc=F("Opera"),dc=F("Trident")||F("MSIE"),ec=F("Edge"),fc=F("Gecko")&&!(-1!=Kb().toLowerCase().indexOf("webkit")&&!F("Edge"))&&!(F("Trident")||F("MSIE"))&&!F("Edge"),gc=-1!=Kb().toLowerCase().indexOf("webkit")&&!F("Edge");function hc(){var a=z.document;return a?a.documentMode:void 0}
var ic;a:{var jc="",kc=function(){var a=Kb();if(fc)return/rv:([^\);]+)(\)|;)/.exec(a);if(ec)return/Edge\/([\d\.]+)/.exec(a);if(dc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(gc)return/WebKit\/(\S+)/.exec(a);if(cc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
kc&&(jc=kc?kc[1]:"");if(dc){var lc=hc();if(null!=lc&&lc>parseFloat(jc)){ic=String(lc);break a}}ic=jc}var mc=ic,nc;if(z.document&&dc){var oc=hc();nc=oc?oc:parseInt(mc,10)||void 0}else nc=void 0;var pc=nc;var qc=ac()||F("iPod"),rc=F("iPad");!F("Android")||Lb();Lb();var sc=F("Safari")&&!(Lb()||F("Coast")||F("Opera")||F("Edge")||F("Edg/")||F("OPR")||F("Firefox")||F("FxiOS")||F("Silk")||F("Android"))&&!(ac()||F("iPad")||F("iPod"));var tc={},vc=null;function wc(a,b){Oa(a);void 0===b&&(b=0);xc();b=tc[b];for(var c=Array(Math.floor(a.length/3)),d=b[64]||"",e=0,f=0;e<a.length-2;e+=3){var g=a[e],h=a[e+1],k=a[e+2],l=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|k>>6];k=b[k&63];c[f++]=""+l+g+h+k}l=0;k=d;switch(a.length-e){case 2:l=a[e+1],k=b[(l&15)<<2]||d;case 1:a=a[e],c[f]=""+b[a>>2]+b[(a&3)<<4|l>>4]+k+d}return c.join("")}
function yc(a){var b=a.length,c=3*b/4;c%3?c=Math.floor(c):-1!="=.".indexOf(a[b-1])&&(c=-1!="=.".indexOf(a[b-2])?c-2:c-1);var d=new Uint8Array(c),e=0;zc(a,function(f){d[e++]=f});
return e!==c?d.subarray(0,e):d}
function zc(a,b){function c(k){for(;d<a.length;){var l=a.charAt(d++),m=vc[l];if(null!=m)return m;if(!/^[\s\xa0]*$/.test(l))throw Error("Unknown base64 encoding at char: "+l);}return k}
xc();for(var d=0;;){var e=c(-1),f=c(0),g=c(64),h=c(64);if(64===h&&-1===e)break;b(e<<2|f>>4);64!=g&&(b(f<<4&240|g>>2),64!=h&&b(g<<6&192|h))}}
function xc(){if(!vc){vc={};for(var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"],c=0;5>c;c++){var d=a.concat(b[c].split(""));tc[c]=d;for(var e=0;e<d.length;e++){var f=d[e];void 0===vc[f]&&(vc[f]=e)}}}}
;var Ac="undefined"!==typeof Uint8Array;function Bc(a){return Ac&&null!=a&&a instanceof Uint8Array}
var Cc={};var Dc;function Ec(){if(Cc!==Cc)throw Error("illegal external caller");}
function Fc(a){Ec();this.oa=a;if(null!=a&&0===a.length)throw Error("ByteString should be constructed with non-empty values");}
Fc.prototype.za=function(){return null==this.oa};
Fc.prototype.sizeBytes=function(){Ec();var a=this.oa;null==a||Bc(a)||("string"===typeof a?a=yc(a):(La(a),a=null));return(a=null==a?a:this.oa=a)?a.length:0};var Gc="function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():void 0;function Hc(a,b){if(Gc)return a[Gc]|=b;if(void 0!==a.M)return a.M|=b;Object.defineProperties(a,{M:{value:b,configurable:!0,writable:!0,enumerable:!1}});return b}
function Ic(a,b){Gc?a[Gc]&&(a[Gc]&=~b):void 0!==a.M&&(a.M&=~b)}
function G(a){var b;Gc?b=a[Gc]:b=a.M;return null==b?0:b}
function Jc(a,b){Gc?a[Gc]=b:void 0!==a.M?a.M=b:Object.defineProperties(a,{M:{value:b,configurable:!0,writable:!0,enumerable:!1}})}
function Kc(a){Hc(a,1);return a}
function Lc(a){return!!(G(a)&2)}
function Pc(a){Hc(a,16);return a}
function Qc(a,b){Jc(b,(a|0)&-51)}
function Rc(a,b){Jc(b,(a|18)&-41)}
;var Sc={};function Tc(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object}
var Uc,Vc,Wc=[];Jc(Wc,23);Vc=Object.freeze(Wc);function Xc(a){if(Lc(a.v))throw Error("Cannot mutate an immutable Message");}
function Yc(a){var b=a.length;(b=b?a[b-1]:void 0)&&Tc(b)?b.g=1:(b={},a.push((b.g=1,b)))}
;function Zc(a){return a.displayName||a.name||"unknown type name"}
function $c(a,b){if(!(a instanceof b))throw Error("Expected instanceof "+Zc(b)+" but got "+(a&&Zc(a.constructor)));return a}
;var ad;function bd(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "object":if(a)if(Array.isArray(a)){if(0!==(G(a)&128))return a=Array.prototype.slice.call(a),Yc(a),a}else{if(Bc(a))return wc(a);if(a instanceof Fc){var b=a.oa;return null==b?"":"string"===typeof b?b:a.oa=wc(b)}}}return a}
;function cd(a,b,c,d){if(null!=a){if(Array.isArray(a))a=dd(a,b,c,void 0!==d);else if(Tc(a)){var e={},f;for(f in a)e[f]=cd(a[f],b,c,d);a=e}else a=b(a,d);return a}}
function dd(a,b,c,d){var e=G(a);d=d?!!(e&16):void 0;a=Array.prototype.slice.call(a);for(var f=0;f<a.length;f++)a[f]=cd(a[f],b,c,d);c(e,a);return a}
function ed(a){return a.Aa===Sc?a.toJSON():bd(a)}
function fd(a){if(!a)return a;if("object"===typeof a){if(Bc(a))return new Uint8Array(a);if(a.Aa===Sc)return a.clone()}return a}
function gd(a,b){a&128&&Yc(b)}
;function hd(a){return a.i||(a.i=a.v[a.j+a.W]={})}
function id(a,b,c){return-1===b?null:b>=a.j?a.i?a.i[b]:void 0:c&&a.i&&(c=a.i[b],null!=c)?c:a.v[b+a.W]}
function I(a,b,c,d){Xc(a);return jd(a,b,c,d)}
function jd(a,b,c,d){a.l&&(a.l=void 0);if(b>=a.j||d)return hd(a)[b]=c,a;a.v[b+a.W]=c;(c=a.i)&&b in c&&delete c[b];return a}
function kd(a,b){a&&Lc(b.v)&&Lc(a.v);return a}
function ld(a,b,c,d,e){var f=id(a,b,d);Array.isArray(f)||(f=Vc);var g=G(f);g&1||Kc(f);if(e)g&2||Hc(f,2),c&1||Object.freeze(f);else{e=!(c&2);var h=g&2;c&1||!h?e&&g&16&&!h&&Ic(f,16):(f=Kc(Array.prototype.slice.call(f)),jd(a,b,f,d))}return f}
function md(a,b,c,d){Xc(a);(c=nd(a,c))&&c!==b&&null!=d&&jd(a,c,void 0,!1);jd(a,b,d)}
function nd(a,b){for(var c=0,d=0;d<b.length;d++){var e=b[d];null!=id(a,e)&&(0!==c&&jd(a,c,void 0,!1),c=e)}return c}
function od(a,b,c){var d=void 0===d?!1:d;var e=id(a,c,d);var f=!1;var g=null==e||"object"!==typeof e||(f=Array.isArray(e))||e.Aa!==Sc?f?new b(e):void 0:e;g!==e&&null!=g&&(jd(a,c,g,d),Hc(g.v,G(a.v)&-33));b=kd(g,a);if(null==b)return b;Lc(a.v)||(e=pd(b),e!==b&&(b=e,jd(a,c,b,d)));return kd(b,a)}
function qd(a,b,c,d,e,f){a.h||(a.h={});var g=a.h[c],h=ld(a,c,3,d,f);if(g)f||(Object.isFrozen(g)?e||(g=Array.prototype.slice.call(g),a.h[c]=g):e&&Object.freeze(g));else{g=[];var k=!!(G(a.v)&16),l=Lc(h);!f&&l&&(h=Kc(Array.prototype.slice.call(h)),jd(a,c,h,d));d=l;for(var m=0;m<h.length;m++){var n=h[m];var r=b;var q=k,y=!1;y=void 0===y?!1:y;q=void 0===q?!1:q;r=Array.isArray(n)?new r(q?Pc(n):n):y?new r:void 0;void 0!==r&&(d=d||Lc(n),g.push(r),l&&Hc(r.v,2))}a.h[c]=g;a=h;b=!d;Object.isFrozen(a)||(c=G(a)|
33,Jc(a,b?c|8:c&-9));(f||e&&l)&&Hc(g,2);(f||e)&&Object.freeze(g)}return g}
function J(a,b,c,d){Xc(a);null!=d?$c(d,b):d=void 0;return jd(a,c,d)}
function rd(a,b,c,d,e){Xc(a);null!=e?$c(e,b):e=void 0;md(a,c,d,e)}
function sd(a,b,c,d,e){Xc(a);if(null!=d){var f=Kc([]);for(var g=!1,h=0;h<d.length;h++)f[h]=$c(d[h],b).v,g=g||Lc(f[h]);a.h||(a.h={});a.h[c]=d;b=f;g?Ic(b,8):Hc(b,8)}else a.h&&(a.h[c]=void 0),f=Vc;return jd(a,c,f,e)}
function td(a,b,c,d){Xc(a);var e=qd(a,c,b,void 0,!1,!1);c=null!=d?$c(d,c):new c;a=ld(a,b,2,void 0,!1);e.push(c);a.push(c.v);Lc(c.v)&&Ic(a,8)}
function ud(a,b){return id(a,b)}
function vd(a,b){a=id(a,b);return null==a?"":a}
;function wd(a,b,c){c=void 0===c?Rc:c;if(null!=a){if(Ac&&a instanceof Uint8Array)return a.length?new Fc(new Uint8Array(a)):Dc||(Dc=new Fc(null));if(Array.isArray(a)){var d=G(a);if(d&2)return a;if(b&&!(d&32)&&(d&16||0===d))return Jc(a,d|2),a;a=dd(a,wd,c,!0);b=G(a);b&4&&b&2&&Object.freeze(a);return a}return a.Aa===Sc?xd(a):a}}
function yd(a,b,c,d,e,f,g){(a=a.h&&a.h[c])?(d=0<a.length?a[0].constructor:void 0,f=G(a),f&2||(a=cb(a,xd),Rc(f,a),Object.freeze(a)),sd(b,d,c,a,e)):I(b,c,wd(d,f,g),e)}
function xd(a){if(Lc(a.v))return a;a=zd(a,!0);Hc(a.v,2);return a}
function zd(a,b){var c=a.v,d=Pc([]),e=a.constructor.h;e&&d.push(e);0!==(G(c)&128)&&Yc(d);b=b||Lc(a.v)?Rc:Qc;e=a.constructor;G(d);ad=d;d=new e(d);ad=void 0;a.ja&&(d.ja=a.ja.slice());e=!!(G(c)&16);for(var f=0;f<c.length;f++){var g=c[f];if(f===c.length-1&&Tc(g))for(var h in g){var k=+h;Number.isNaN(k)?hd(d)[k]=g[k]:yd(a,d,k,g[h],!0,e,b)}else yd(a,d,f-a.W,g,!1,e,b)}return d}
;function L(a,b,c){null==a&&(a=ad);ad=void 0;var d=this.constructor.i||0,e=0<d,f=this.constructor.h,g=!1;if(null==a){a=f?[f]:[];var h=!0;Jc(a,48)}else{if(!Array.isArray(a))throw Error();if(f&&f!==a[0])throw Error();var k=Hc(a,0),l=k;if(h=0!==(16&l))(g=0!==(32&l))||(l|=32);if(e)if(128&l)d=0;else{if(0<a.length){var m=a[a.length-1];if(Tc(m)&&"g"in m){d=0;l|=128;delete m.g;var n=!0,r;for(r in m){n=!1;break}n&&a.pop()}}}else if(128&l)throw Error();k!==l&&Jc(a,l)}this.W=(f?0:-1)-d;this.h=void 0;this.v=a;
a:{f=this.v.length;d=f-1;if(f&&(f=this.v[d],Tc(f))){this.i=f;this.j=d-this.W;break a}void 0!==b&&-1<b?(this.j=Math.max(b,d+1-this.W),this.i=void 0):this.j=Number.MAX_VALUE}if(!e&&this.i&&"g"in this.i)throw Error('Unexpected "g" flag in sparse object of message that is not a group type.');if(c){b=h&&!g&&!0;e=this.j;var q;for(h=0;h<c.length;h++)g=c[h],g<e?(g+=this.W,(d=a[g])?Ad(d,b):a[g]=Vc):(q||(q=hd(this)),(d=q[g])?Ad(d,b):q[g]=Vc)}}
L.prototype.toJSON=function(){var a=this.v,b;Uc?b=a:b=dd(a,ed,gd);return b};
function Bd(a){Uc=!0;try{return JSON.stringify(a.toJSON(),Cd)}finally{Uc=!1}}
L.prototype.clone=function(){var a=dd(this.v,fd,Qc);Pc(a);ad=a;a=new this.constructor(a);ad=void 0;Dd(a,this);return a};
function pd(a){if(Lc(a.v)){var b=zd(a,!1);b.l=a;a=b}return a}
function Ad(a,b){if(Array.isArray(a)){var c=G(a),d=1;!b||c&2||(d|=16);(c&d)!==d&&Jc(a,c|d)}}
L.prototype.Aa=Sc;L.prototype.toString=function(){return this.v.toString()};
function Cd(a,b){return bd(b)}
function Dd(a,b){b.ja&&(a.ja=b.ja.slice());var c=b.h;if(c){b=b.i;for(var d in c){var e=c[d];if(e){var f=!(!b||!b[d]),g=+d;if(Array.isArray(e)){if(e.length){var h=a,k=e[0].constructor,l=Lc(h.v);k=qd(h,k,g,f,l,l);f=ld(h,g,3,f,l);if(!l&&f&&!(G(f)&8)){for(l=0;l<k.length;l++)g=k[l],h=pd(g),g!==h&&(k[l]=h,f[l]=k[l].v);Hc(f,8)}for(l=0;l<Math.min(k.length,e.length);l++)Dd(k[l],e[l])}}else throw Error("unexpected object: type: "+La(e)+": "+e);}}}}
;var Ed=window;sb("csi.gstatic.com");sb("googleads.g.doubleclick.net");sb("partner.googleadservices.com");sb("pubads.g.doubleclick.net");sb("securepubads.g.doubleclick.net");sb("tpc.googlesyndication.com");function Fd(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
p=Fd.prototype;p.clone=function(){return new Fd(this.x,this.y)};
p.equals=function(a){return a instanceof Fd&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
p.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
p.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
p.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Gd(a,b){this.width=a;this.height=b}
p=Gd.prototype;p.clone=function(){return new Gd(this.width,this.height)};
p.aspectRatio=function(){return this.width/this.height};
p.za=function(){return!(this.width*this.height)};
p.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
p.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
p.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Hd(){var a=document;var b="IFRAME";"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Id(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Jd(a){var b=C("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||z.$googDebugFname||b}catch(g){e="Not available",c=!0}b=Kd(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,Ld[c])c=Ld[c];else{c=String(c);if(!Ld[c]){var f=/function\s+([^\(]+)/m.exec(c);Ld[c]=f?f[1]:"[Anonymous]"}c=Ld[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return{message:a.message,name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:a.stack}}
function Kd(a,b){b||(b={});b[Md(a)]=!0;var c=a.stack||"";(a=a.cause)&&!b[Md(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=Kd(a,b));return c}
function Md(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var Ld={};/*

 SPDX-License-Identifier: Apache-2.0
*/
var Nd;try{new URL("s://g"),Nd=!0}catch(a){Nd=!1}var Od=Nd;function Pd(a,b){a.removeAttribute("srcdoc");if(b instanceof Hb)b instanceof Hb&&b.constructor===Hb?b=b.h:(La(b),b="type_error:SafeUrl");else{b:if(Od){try{var c=new URL(b)}catch(d){c="https:";break b}c=c.protocol}else c:{c=document.createElement("a");try{c.href=b}catch(d){c=void 0;break c}c=c.protocol;c=":"===c||""===c?"https:":c}b="javascript:"!==c?b:void 0}void 0!==b&&(a.src=b);for(b="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-storage-access-by-user-activation".split(" ");0<
a.sandbox.length;)a.sandbox.remove(a.sandbox.item(0));for(c=0;c<b.length;c++)a.sandbox.supports&&!a.sandbox.supports(b[c])||a.sandbox.add(b[c])}
;function Qd(a){this.Ab=a}
function Rd(a){return new Qd(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var Sd=[Rd("data"),Rd("http"),Rd("https"),Rd("mailto"),Rd("ftp"),new Qd(function(a){return/^[^:]*([/?#]|$)/.test(a)})];
function Td(a,b){b=void 0===b?Sd:b;for(var c=0;c<b.length;++c){var d=b[c];if(d instanceof Qd&&d.Ab(a))return new Hb(a,Ib)}}
function Wd(a){var b=void 0===b?Sd:b;return Td(a,b)||Jb}
;function Xd(a){var b=Yd;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a(b[c],c,b)}
function Zd(){var a=[];Xd(function(b){a.push(b)});
return a}
var Yd={Kb:"allow-forms",Lb:"allow-modals",Mb:"allow-orientation-lock",Nb:"allow-pointer-lock",Ob:"allow-popups",Pb:"allow-popups-to-escape-sandbox",Qb:"allow-presentation",Rb:"allow-same-origin",Sb:"allow-scripts",Tb:"allow-top-navigation",Ub:"allow-top-navigation-by-user-activation"},$d=ab(function(){return Zd()});
function ae(){var a=be(),b={};E($d(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
function be(){var a=void 0===a?document:a;return a.createElement("iframe")}
;var ce=(new Date).getTime();function de(a){if(!a)return"";if(/^about:(?:blank|srcdoc)$/.test(a))return window.origin||"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==
c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;var ee="client_dev_domain client_dev_regex_map client_dev_root_url client_rollout_override expflag forcedCapability jsfeat jsmode mods".split(" ");ia(ee);function fe(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;m=l=0}
function b(n){for(var r=g,q=0;64>q;q+=4)r[q/4]=n[q]<<24|n[q+1]<<16|n[q+2]<<8|n[q+3];for(q=16;80>q;q++)n=r[q-3]^r[q-8]^r[q-14]^r[q-16],r[q]=(n<<1|n>>>31)&4294967295;n=e[0];var y=e[1],A=e[2],H=e[3],K=e[4];for(q=0;80>q;q++){if(40>q)if(20>q){var M=H^y&(A^H);var O=1518500249}else M=y^A^H,O=1859775393;else 60>q?(M=y&A|H&(y|A),O=2400959708):(M=y^A^H,O=3395469782);M=((n<<5|n>>>27)&4294967295)+M+K+O+r[q]&4294967295;K=H;H=A;A=(y<<30|y>>>2)&4294967295;y=n;n=M}e[0]=e[0]+n&4294967295;e[1]=e[1]+y&4294967295;e[2]=
e[2]+A&4294967295;e[3]=e[3]+H&4294967295;e[4]=e[4]+K&4294967295}
function c(n,r){if("string"===typeof n){n=unescape(encodeURIComponent(n));for(var q=[],y=0,A=n.length;y<A;++y)q.push(n.charCodeAt(y));n=q}r||(r=n.length);q=0;if(0==l)for(;q+64<r;)b(n.slice(q,q+64)),q+=64,m+=64;for(;q<r;)if(f[l++]=n[q++],m++,64==l)for(l=0,b(f);q+64<r;)b(n.slice(q,q+64)),q+=64,m+=64}
function d(){var n=[],r=8*m;56>l?c(h,56-l):c(h,64-(l-56));for(var q=63;56<=q;q--)f[q]=r&255,r>>>=8;b(f);for(q=r=0;5>q;q++)for(var y=24;0<=y;y-=8)n[r++]=e[q]>>y&255;return n}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,m;a();return{reset:a,update:c,digest:d,pb:function(){for(var n=d(),r="",q=0;q<n.length;q++)r+="0123456789ABCDEF".charAt(Math.floor(n[q]/16))+"0123456789ABCDEF".charAt(n[q]%16);return r}}}
;function ge(a,b,c){var d=String(z.location.href);return d&&a&&b?[b,he(de(d),a,c||null)].join(" "):null}
function he(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],E(d,function(h){e.push(h)}),ie(e.join(" "));
var f=[],g=[];E(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];E(d,function(h){e.push(h)});
a=ie(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function ie(a){var b=fe();b.update(a);return b.pb().toLowerCase()}
;var je={};function ke(a){this.h=a||{cookie:""}}
p=ke.prototype;p.isEnabled=function(){if(!z.navigator.cookieEnabled)return!1;if(!this.za())return!0;this.set("TESTCOOKIESENABLED","1",{Ka:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
p.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.lc;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.Ka}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString();this.h.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+
e:"")};
p.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=ub(d[e]);if(0==f.lastIndexOf(c,0))return f.slice(c.length);if(f==a)return""}return b};
p.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{Ka:0,path:b,domain:c});return d};
p.za=function(){return!this.h.cookie};
p.clear=function(){for(var a=(this.h.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=ub(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var le=new ke("undefined"==typeof document?null:document);function me(a){return!!je.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function ne(a,b,c,d){(a=z[a])||(a=(new ke(document)).get(b));return a?ge(a,c,d):null}
function oe(a){var b=void 0===b?!1:b;var c=de(String(z.location.href)),d=[];var e=b;e=void 0===e?!1:e;var f=z.__SAPISID||z.__APISID||z.__3PSAPISID||z.__OVERRIDE_SID;me(e)&&(f=f||z.__1PSAPISID);if(f)e=!0;else{var g=new ke(document);f=g.get("SAPISID")||g.get("APISID")||g.get("__Secure-3PAPISID")||g.get("SID");me(e)&&(f=f||g.get("__Secure-1PAPISID"));e=!!f}e&&(e=(c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:"))?z.__SAPISID:z.__APISID,e||(e=new ke(document),
e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID")),(e=e?ge(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e),c&&me(b)&&((b=ne("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=ne("__3PSAPISID","__Secure-3PAPISID","SAPISID3PHASH",a))&&d.push(a)));return 0==d.length?null:d.join(" ")}
;function pe(){this.j=this.j;this.o=this.o}
pe.prototype.j=!1;pe.prototype.dispose=function(){this.j||(this.j=!0,this.ba())};
pe.prototype.ba=function(){if(this.o)for(;this.o.length;)this.o.shift()()};function qe(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
qe.prototype.stopPropagation=function(){this.j=!0};
qe.prototype.preventDefault=function(){this.defaultPrevented=!0};var re=function(){if(!z.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{z.addEventListener("test",function(){},b),z.removeEventListener("test",function(){},b)}catch(c){}return a}();function se(a,b){qe.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
D(se,qe);var te={2:"touch",3:"pen",4:"mouse"};
se.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(fc){a:{try{bc(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:te[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&se.O.preventDefault.call(this)};
se.prototype.stopPropagation=function(){se.O.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
se.prototype.preventDefault=function(){se.O.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var ue="closure_listenable_"+(1E6*Math.random()|0);var ve=0;function we(a,b,c,d,e){this.listener=a;this.proxy=null;this.src=b;this.type=c;this.capture=!!d;this.ya=e;this.key=++ve;this.ka=this.ta=!1}
function xe(a){a.ka=!0;a.listener=null;a.proxy=null;a.src=null;a.ya=null}
;function ye(a){this.src=a;this.listeners={};this.h=0}
ye.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=ze(a,b,d,e);-1<g?(b=a[g],c||(b.ta=!1)):(b=new we(b,this.src,f,!!d,e),b.ta=c,a.push(b));return b};
ye.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=ze(e,b,c,d);return-1<b?(xe(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function Ae(a,b){var c=b.type;c in a.listeners&&eb(a.listeners[c],b)&&(xe(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function ze(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.ka&&f.listener==b&&f.capture==!!c&&f.ya==d)return e}return-1}
;var Be="closure_lm_"+(1E6*Math.random()|0),Ce={},De=0;function Ee(a,b,c,d,e){if(d&&d.once)Fe(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)Ee(a,b[f],c,d,e);else c=Ge(c),a&&a[ue]?a.X(b,c,Pa(d)?!!d.capture:!!d,e):He(a,b,c,!1,d,e)}
function He(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Pa(e)?!!e.capture:!!e,h=Ie(a);h||(a[Be]=h=new ye(a));c=h.add(b,c,d,g,f);if(!c.proxy){d=Je();c.proxy=d;d.src=a;d.listener=c;if(a.addEventListener)re||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(Ke(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");De++}}
function Je(){function a(c){return b.call(a.src,a.listener,c)}
var b=Le;return a}
function Fe(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)Fe(a,b[f],c,d,e);else c=Ge(c),a&&a[ue]?a.h.add(String(b),c,!0,Pa(d)?!!d.capture:!!d,e):He(a,b,c,!0,d,e)}
function Me(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)Me(a,b[f],c,d,e);else(d=Pa(d)?!!d.capture:!!d,c=Ge(c),a&&a[ue])?a.h.remove(String(b),c,d,e):a&&(a=Ie(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=ze(b,c,d,e)),(c=-1<a?b[a]:null)&&Ne(c))}
function Ne(a){if("number"!==typeof a&&a&&!a.ka){var b=a.src;if(b&&b[ue])Ae(b.h,a);else{var c=a.type,d=a.proxy;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(Ke(c),d):b.addListener&&b.removeListener&&b.removeListener(d);De--;(c=Ie(b))?(Ae(c,a),0==c.h&&(c.src=null,b[Be]=null)):xe(a)}}}
function Ke(a){return a in Ce?Ce[a]:Ce[a]="on"+a}
function Le(a,b){if(a.ka)a=!0;else{b=new se(b,this);var c=a.listener,d=a.ya||a.src;a.ta&&Ne(a);a=c.call(d,b)}return a}
function Ie(a){a=a[Be];return a instanceof ye?a:null}
var Oe="__closure_events_fn_"+(1E9*Math.random()>>>0);function Ge(a){if("function"===typeof a)return a;a[Oe]||(a[Oe]=function(b){return a.handleEvent(b)});
return a[Oe]}
;function Pe(){pe.call(this);this.h=new ye(this);this.V=this;this.C=null}
D(Pe,pe);Pe.prototype[ue]=!0;Pe.prototype.addEventListener=function(a,b,c,d){Ee(this,a,b,c,d)};
Pe.prototype.removeEventListener=function(a,b,c,d){Me(this,a,b,c,d)};
function Qe(a,b){var c=a.C;if(c){var d=[];for(var e=1;c;c=c.C)d.push(c),++e}a=a.V;c=b.type||b;"string"===typeof b?b=new qe(b,a):b instanceof qe?b.target=b.target||a:(e=b,b=new qe(c,a),ob(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=Re(g,c,!0,b)&&e}b.j||(g=b.h=a,e=Re(g,c,!0,b)&&e,b.j||(e=Re(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=Re(g,c,!1,b)&&e}
Pe.prototype.ba=function(){Pe.O.ba.call(this);if(this.h){var a=this.h,b=0,c;for(c in a.listeners){for(var d=a.listeners[c],e=0;e<d.length;e++)++b,xe(d[e]);delete a.listeners[c];a.h--}}this.C=null};
Pe.prototype.X=function(a,b,c,d){return this.h.add(String(a),b,!1,c,d)};
function Re(a,b,c,d){b=a.h.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.ka&&g.capture==c){var h=g.listener,k=g.ya||g.src;g.ta&&Ae(a.h,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function Se(a){Pe.call(this);var b=this;this.G=this.l=0;this.J=null!=a?a:{L:function(e,f){return setTimeout(e,f)},
Z:function(e){clearTimeout(e)}};
var c,d;this.i=null!=(d=null==(c=window.navigator)?void 0:c.onLine)?d:!0;this.m=function(){return x(function(e){return w(e,Te(b),0)})};
window.addEventListener("offline",this.m);window.addEventListener("online",this.m);this.G||Ue(this)}
v(Se,Pe);function Ve(){var a=We;Se.h||(Se.h=new Se(a));return Se.h}
Se.prototype.dispose=function(){window.removeEventListener("offline",this.m);window.removeEventListener("online",this.m);this.J.Z(this.G);delete Se.h};
Se.prototype.I=function(){return this.i};
function Ue(a){a.G=a.J.L(function(){var b;return x(function(c){if(1==c.h)return a.i?(null==(b=window.navigator)?0:b.onLine)?c.s(3):w(c,Te(a),3):w(c,Te(a),3);Ue(a);c.h=0})},3E4)}
function Te(a,b){return a.u?a.u:a.u=new Promise(function(c){var d,e,f,g;return x(function(h){switch(h.h){case 1:return d=window.AbortController?new window.AbortController:void 0,f=null==(e=d)?void 0:e.signal,g=!1,wa(h,2,3),d&&(a.l=a.J.L(function(){d.abort()},b||2E4)),w(h,fetch("/generate_204",{method:"HEAD",
signal:f}),5);case 5:g=!0;case 3:za(h);a.u=void 0;a.l&&(a.J.Z(a.l),a.l=0);g!==a.i&&(a.i=g,a.i?Qe(a,"networkstatus-online"):Qe(a,"networkstatus-offline"));c(g);Ba(h);break;case 2:ya(h),g=!1,h.s(3)}})})}
;function Xe(){this.data_=[];this.h=-1}
Xe.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&Number.isInteger(a)&&this.data_[a]!==b&&(this.data_[a]=b,this.h=-1)};
Xe.prototype.get=function(a){return!!this.data_[a]};
function Ye(a){-1===a.h&&(a.h=db(a.data_,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.h}
;function Ze(a){L.call(this,a,-1,$e)}
v(Ze,L);function af(a,b){return I(a,2,b)}
function bf(a,b){return I(a,3,b)}
function cf(a,b){return I(a,4,b)}
function df(a,b){return I(a,5,b)}
function ef(a,b){return I(a,9,b)}
function ff(a,b){return sd(a,gf,10,b)}
function hf(a,b){return I(a,11,b)}
function jf(a,b){return I(a,1,b)}
function kf(a,b){return I(a,7,b)}
function gf(a){L.call(this,a)}
v(gf,L);var $e=[10,6];var lf="platform platformVersion architecture model uaFullVersion bitness fullVersionList wow64".split(" ");function mf(a){var b;return null!=(b=a.google_tag_data)?b:a.google_tag_data={}}
function nf(a){var b,c;return"function"===typeof(null==(b=a.navigator)?void 0:null==(c=b.userAgentData)?void 0:c.getHighEntropyValues)}
function of(){var a=window;if(!nf(a))return null;var b=mf(a);if(b.uach_promise)return b.uach_promise;a=a.navigator.userAgentData.getHighEntropyValues(lf).then(function(c){null!=b.uach||(b.uach=c);return c});
return b.uach_promise=a}
function pf(a){var b;return hf(ff(df(af(jf(cf(kf(ef(bf(new Ze,a.architecture||""),a.bitness||""),a.mobile||!1),a.model||""),a.platform||""),a.platformVersion||""),a.uaFullVersion||""),(null==(b=a.fullVersionList)?void 0:b.map(function(c){var d=new gf;d=I(d,1,c.brand);return I(d,2,c.version)}))||[]),a.wow64||!1)}
function qf(){var a,b;return null!=(b=null==(a=of())?void 0:a.then(function(c){return pf(c)}))?b:null}
;function rf(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
rf.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function sf(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;var tf;function uf(){var a=z.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!F("Presto")&&(a=function(){var e=Hd();e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=Va(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!F("Trident")&&!F("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.Ra;c.Ra=null;e()}};
return function(e){d.next={Ra:e};d=d.next;b.port2.postMessage(0)}}return function(e){z.setTimeout(e,0)}}
;function vf(){this.i=this.h=null}
vf.prototype.add=function(a,b){var c=wf.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
vf.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var wf=new rf(function(){return new xf},function(a){return a.reset()});
function xf(){this.next=this.scope=this.h=null}
xf.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
xf.prototype.reset=function(){this.next=this.scope=this.h=null};var yf,zf=!1,Af=new vf;function Bf(a,b){yf||Cf();zf||(yf(),zf=!0);Af.add(a,b)}
function Cf(){if(z.Promise&&z.Promise.resolve){var a=z.Promise.resolve(void 0);yf=function(){a.then(Df)}}else yf=function(){var b=Df;
"function"!==typeof z.setImmediate||z.Window&&z.Window.prototype&&!F("Edge")&&z.Window.prototype.setImmediate==z.setImmediate?(tf||(tf=uf()),tf(b)):z.setImmediate(b)}}
function Df(){for(var a;a=Af.remove();){try{a.h.call(a.scope)}catch(b){$b(b)}sf(wf,a)}zf=!1}
;function Ef(a,b){this.h=a[z.Symbol.iterator]();this.i=b}
Ef.prototype[Symbol.iterator]=function(){return this};
Ef.prototype.next=function(){var a=this.h.next();return{value:a.done?void 0:this.i.call(void 0,a.value),done:a.done}};
function Ff(a,b){return new Ef(a,b)}
;function Gf(){this.blockSize=-1}
;function Hf(){this.blockSize=-1;this.blockSize=64;this.h=[];this.o=[];this.m=[];this.j=[];this.j[0]=128;for(var a=1;a<this.blockSize;++a)this.j[a]=0;this.l=this.i=0;this.reset()}
D(Hf,Gf);Hf.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.l=this.i=0};
function If(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
Hf.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.o,f=this.i;d<b;){if(0==f)for(;d<=c;)If(this,a,d),d+=this.blockSize;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.blockSize){If(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){If(this,e);f=0;break}}this.i=f;this.l+=b}};
Hf.prototype.digest=function(){var a=[],b=8*this.l;56>this.i?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;56<=c;c--)this.o[c]=b&255,b/=256;If(this,this.o);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function Jf(){}
Jf.prototype.next=function(){return Kf};
var Kf={done:!0,value:void 0};function Lf(a){return{value:a,done:!1}}
Jf.prototype.K=function(){return this};function Mf(a){if(a instanceof Nf||a instanceof Of||a instanceof Pf)return a;if("function"==typeof a.next)return new Nf(function(){return a});
if("function"==typeof a[Symbol.iterator])return new Nf(function(){return a[Symbol.iterator]()});
if("function"==typeof a.K)return new Nf(function(){return a.K()});
throw Error("Not an iterator or iterable.");}
function Nf(a){this.i=a}
Nf.prototype.K=function(){return new Of(this.i())};
Nf.prototype[Symbol.iterator]=function(){return new Pf(this.i())};
Nf.prototype.h=function(){return new Pf(this.i())};
function Of(a){this.i=a}
v(Of,Jf);Of.prototype.next=function(){return this.i.next()};
Of.prototype[Symbol.iterator]=function(){return new Pf(this.i)};
Of.prototype.h=function(){return new Pf(this.i)};
function Pf(a){Nf.call(this,function(){return a});
this.j=a}
v(Pf,Nf);Pf.prototype.next=function(){return this.j.next()};function Qf(a,b){this.i={};this.h=[];this.j=this.size=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Qf)for(c=Rf(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Rf(a){Sf(a);return a.h.concat()}
p=Qf.prototype;p.has=function(a){return Tf(this.i,a)};
p.equals=function(a,b){if(this===a)return!0;if(this.size!=a.size)return!1;b=b||Uf;Sf(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function Uf(a,b){return a===b}
p.za=function(){return 0==this.size};
p.clear=function(){this.i={};this.j=this.size=this.h.length=0};
p.remove=function(a){return this.delete(a)};
p.delete=function(a){return Tf(this.i,a)?(delete this.i[a],--this.size,this.j++,this.h.length>2*this.size&&Sf(this),!0):!1};
function Sf(a){if(a.size!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];Tf(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.size!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],Tf(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
p.get=function(a,b){return Tf(this.i,a)?this.i[a]:b};
p.set=function(a,b){Tf(this.i,a)||(this.size+=1,this.h.push(a),this.j++);this.i[a]=b};
p.forEach=function(a,b){for(var c=Rf(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
p.clone=function(){return new Qf(this)};
p.keys=function(){return Mf(this.K(!0)).h()};
p.values=function(){return Mf(this.K(!1)).h()};
p.entries=function(){var a=this;return Ff(this.keys(),function(b){return[b,a.get(b)]})};
p.K=function(a){Sf(this);var b=0,c=this.j,d=this,e=new Jf;e.next=function(){if(c!=d.j)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)return Kf;var f=d.h[b++];return Lf(a?f:d.i[f])};
return e};
function Tf(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
;var Vf=z.JSON.stringify;function Wf(){var a=this;this.promise=new Promise(function(b,c){a.resolve=b;a.reject=c})}
;function Xf(a){this.h=0;this.u=void 0;this.l=this.i=this.j=null;this.o=this.m=!1;if(a!=Za)try{var b=this;a.call(void 0,function(c){ug(b,2,c)},function(c){ug(b,3,c)})}catch(c){ug(this,3,c)}}
function vg(){this.next=this.context=this.i=this.j=this.h=null;this.l=!1}
vg.prototype.reset=function(){this.context=this.i=this.j=this.h=null;this.l=!1};
var wg=new rf(function(){return new vg},function(a){a.reset()});
function xg(a,b,c){var d=wg.get();d.j=a;d.i=b;d.context=c;return d}
Xf.prototype.then=function(a,b,c){return yg(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Xf.prototype.$goog_Thenable=!0;Xf.prototype.cancel=function(a){if(0==this.h){var b=new zg(a);Bf(function(){Ag(this,b)},this)}};
function Ag(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.l||(d++,g.h==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?Ag(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):Bg(c),Cg(c,e,3,b)))}a.j=null}else ug(a,3,b)}
function Dg(a,b){a.i||2!=a.h&&3!=a.h||Eg(a);a.l?a.l.next=b:a.i=b;a.l=b}
function yg(a,b,c,d){var e=xg(null,null,null);e.h=new Xf(function(f,g){e.j=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.i=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof zg?g(h):f(k)}catch(l){g(l)}}:g});
e.h.j=a;Dg(a,e);return e.h}
Xf.prototype.G=function(a){this.h=0;ug(this,2,a)};
Xf.prototype.V=function(a){this.h=0;ug(this,3,a)};
function ug(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.G,f=a.V;if(d instanceof Xf){Dg(d,xg(e||Za,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(l){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Pa(d))try{var k=d.then;if("function"===typeof k){Fg(d,k,e,f,a);g=!0;break a}}catch(l){f.call(a,l);g=!0;break a}g=!1}}}g||(a.u=c,a.h=b,a.j=null,Eg(a),3!=b||c instanceof zg||Gg(a,c))}}
function Fg(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Eg(a){a.m||(a.m=!0,Bf(a.C,a))}
function Bg(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
Xf.prototype.C=function(){for(var a;a=Bg(this);)Cg(this,a,this.h,this.u);this.m=!1};
function Cg(a,b,c,d){if(3==c&&b.i&&!b.l)for(;a&&a.o;a=a.j)a.o=!1;if(b.h)b.h.j=null,Hg(b,c,d);else try{b.l?b.j.call(b.context):Hg(b,c,d)}catch(e){Ig.call(null,e)}sf(wg,b)}
function Hg(a,b,c){2==b?a.j.call(a.context,c):a.i&&a.i.call(a.context,c)}
function Gg(a,b){a.o=!0;Bf(function(){a.o&&Ig.call(null,b)})}
var Ig=$b;function zg(a){Xa.call(this,a)}
D(zg,Xa);zg.prototype.name="cancel";function N(a){pe.call(this);this.u=1;this.l=[];this.m=0;this.h=[];this.i={};this.C=!!a}
D(N,pe);p=N.prototype;p.subscribe=function(a,b,c){var d=this.i[a];d||(d=this.i[a]=[]);var e=this.u;this.h[e]=a;this.h[e+1]=b;this.h[e+2]=c;this.u=e+3;d.push(e);return e};
function Jg(a,b,c){var d=Kg;if(a=d.i[a]){var e=d.h;(a=a.find(function(f){return e[f+1]==b&&e[f+2]==c}))&&d.na(a)}}
p.na=function(a){var b=this.h[a];if(b){var c=this.i[b];0!=this.m?(this.l.push(a),this.h[a+1]=function(){}):(c&&eb(c,a),delete this.h[a],delete this.h[a+1],delete this.h[a+2])}return!!b};
p.ea=function(a,b){var c=this.i[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.C)for(e=0;e<c.length;e++){var g=c[e];Lg(this.h[g+1],this.h[g+2],d)}else{this.m++;try{for(e=0,f=c.length;e<f&&!this.j;e++)g=c[e],this.h[g+1].apply(this.h[g+2],d)}finally{if(this.m--,0<this.l.length&&0==this.m)for(;c=this.l.pop();)this.na(c)}}return 0!=e}return!1};
function Lg(a,b,c){Bf(function(){a.apply(b,c)})}
p.clear=function(a){if(a){var b=this.i[a];b&&(b.forEach(this.na,this),delete this.i[a])}else this.h.length=0,this.i={}};
p.ba=function(){N.O.ba.call(this);this.clear();this.l.length=0};function Mg(a){this.h=a}
Mg.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,Vf(b))};
Mg.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Mg.prototype.remove=function(a){this.h.remove(a)};function Ng(a){this.h=a}
D(Ng,Mg);function Og(a){this.data=a}
function Pg(a){return void 0===a||a instanceof Og?a:new Og(a)}
Ng.prototype.set=function(a,b){Ng.O.set.call(this,a,Pg(b))};
Ng.prototype.i=function(a){a=Ng.O.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Ng.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function Qg(a){this.h=a}
D(Qg,Ng);Qg.prototype.set=function(a,b,c){if(b=Pg(b)){if(c){if(c<Date.now()){Qg.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Date.now()}Qg.O.set.call(this,a,b)};
Qg.prototype.i=function(a){var b=Qg.O.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Date.now()||c&&c>Date.now())Qg.prototype.remove.call(this,a);else return b}};function Rg(){}
;function Sg(){}
D(Sg,Rg);Sg.prototype[Symbol.iterator]=function(){return Mf(this.K(!0)).h()};
Sg.prototype.clear=function(){var a=Array.from(this);a=u(a);for(var b=a.next();!b.done;b=a.next())this.remove(b.value)};function Tg(a){this.h=a}
D(Tg,Sg);p=Tg.prototype;p.set=function(a,b){try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
p.get=function(a){a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
p.remove=function(a){this.h.removeItem(a)};
p.K=function(a){var b=0,c=this.h,d=new Jf;d.next=function(){if(b>=c.length)return Kf;var e=c.key(b++);if(a)return Lf(e);e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return Lf(e)};
return d};
p.clear=function(){this.h.clear()};
p.key=function(a){return this.h.key(a)};function Ug(){var a=null;try{a=window.localStorage||null}catch(b){}this.h=a}
D(Ug,Tg);function Vg(a,b){this.i=a;this.h=null;var c;if(c=dc)c=!(9<=Number(pc));if(c){Wg||(Wg=new Qf);this.h=Wg.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),Wg.set(a,this.h));try{this.h.load(this.i)}catch(d){this.h=null}}}
D(Vg,Sg);var Xg={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},Wg=null;function Yg(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return Xg[b]})}
p=Vg.prototype;p.set=function(a,b){this.h.setAttribute(Yg(a),b);Zg(this)};
p.get=function(a){a=this.h.getAttribute(Yg(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
p.remove=function(a){this.h.removeAttribute(Yg(a));Zg(this)};
p.K=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new Jf;d.next=function(){if(b>=c.length)return Kf;var e=c[b++];if(a)return Lf(decodeURIComponent(e.nodeName.replace(/\./g,"%")).slice(1));e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return Lf(e)};
return d};
p.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);Zg(this)};
function Zg(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function $g(a,b){this.i=a;this.h=b+"::"}
D($g,Sg);$g.prototype.set=function(a,b){this.i.set(this.h+a,b)};
$g.prototype.get=function(a){return this.i.get(this.h+a)};
$g.prototype.remove=function(a){this.i.remove(this.h+a)};
$g.prototype.K=function(a){var b=this.i[Symbol.iterator](),c=this,d=new Jf;d.next=function(){var e=b.next();if(e.done)return e;for(e=e.value;e.slice(0,c.h.length)!=c.h;){e=b.next();if(e.done)return e;e=e.value}return Lf(a?e.slice(c.h.length):c.i.get(e))};
return d};function ah(a){this.name=a}
;var bh=new ah("rawColdConfigGroup");var ch=new ah("rawHotConfigGroup");function dh(a){L.call(this,a)}
v(dh,L);dh.prototype.getKey=function(){return id(this,1)};
dh.prototype.S=function(){return ud(this,2===nd(this,eh)?2:-1)};
var eh=[2,3,4,5,6];function fh(a){L.call(this,a)}
v(fh,L);function gh(a){L.call(this,a)}
v(gh,L);function hh(a){L.call(this,a,-1,ih)}
v(hh,L);var ih=[2];function jh(a){L.call(this,a,-1,kh)}
v(jh,L);jh.prototype.getPlayerType=function(){return id(this,36)};
jh.prototype.setHomeGroupInfo=function(a){return J(this,hh,81,a)};
var kh=[9,66,24,32,86,100,101];function lh(a){L.call(this,a,-1,mh)}
v(lh,L);var mh=[15,26,28];function nh(a){L.call(this,a,-1,oh)}
v(nh,L);var oh=[5];function ph(a){L.call(this,a)}
v(ph,L);function qh(a){L.call(this,a,-1,rh)}
v(qh,L);qh.prototype.setSafetyMode=function(a){return I(this,5,a)};
var rh=[12];function sh(a){L.call(this,a,-1,th)}
v(sh,L);var th=[12];var uh={Zb:"WEB_DISPLAY_MODE_UNKNOWN",Vb:"WEB_DISPLAY_MODE_BROWSER",Xb:"WEB_DISPLAY_MODE_MINIMAL_UI",Yb:"WEB_DISPLAY_MODE_STANDALONE",Wb:"WEB_DISPLAY_MODE_FULLSCREEN"};function vh(a){L.call(this,a,-1,wh)}
v(vh,L);function xh(a){L.call(this,a)}
v(xh,L);xh.prototype.getKey=function(){return vd(this,1)};
xh.prototype.S=function(){return vd(this,2)};
var wh=[4,5];function yh(a){L.call(this,a)}
v(yh,L);function zh(a){L.call(this,a)}
v(zh,L);var Ah=[2,3,4];function Bh(a){L.call(this,a)}
v(Bh,L);function Ch(a){L.call(this,a)}
v(Ch,L);function Dh(a){L.call(this,a)}
v(Dh,L);function Eh(a){L.call(this,a,-1,Fh)}
v(Eh,L);var Fh=[10,17];function Gh(a){L.call(this,a)}
v(Gh,L);function Hh(a){L.call(this,a)}
v(Hh,L);function Ih(a){L.call(this,a)}
v(Ih,L);function Jh(a){L.call(this,a,449)}
v(Jh,L);
var Kh=[23,24,11,6,7,5,2,3,13,20,21,22,28,32,37,229,241,45,59,225,288,72,73,78,208,156,202,215,74,76,79,80,111,85,91,97,100,102,105,119,126,127,136,146,148,151,157,158,159,163,164,168,444,176,222,383,177,178,179,411,184,188,189,190,191,193,194,195,196,197,198,199,200,201,402,320,203,204,205,206,258,259,260,261,327,209,219,226,227,232,233,234,240,244,247,248,249,251,256,257,266,254,255,270,272,278,291,293,300,304,308,309,310,311,313,314,319,321,323,324,328,330,331,332,334,337,338,340,344,348,350,351,
352,353,354,355,356,357,358,361,363,364,368,369,370,373,374,375,378,380,381,388,389,403,410,412,429,413,414,415,416,417,418,430,423,424,425,426,427,431,117,439,441,448];function Lh(a){L.call(this,a)}
v(Lh,L);function Mh(a){L.call(this,a)}
v(Mh,L);Mh.prototype.getPlaylistId=function(){return ud(this,2===nd(this,Nh)?2:-1)};
var Nh=[1,2];function Oh(a){L.call(this,a,-1,Ph)}
v(Oh,L);var Ph=[3];var Qh=z.window,Rh,Sh,Th=(null==Qh?void 0:null==(Rh=Qh.yt)?void 0:Rh.config_)||(null==Qh?void 0:null==(Sh=Qh.ytcfg)?void 0:Sh.data_)||{};B("yt.config_",Th);function Uh(){var a=arguments;1<a.length?Th[a[0]]=a[1]:1===a.length&&Object.assign(Th,a[0])}
function P(a,b){return a in Th?Th[a]:b}
function Vh(){return P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS")}
function Wh(){var a=Th.EXPERIMENT_FLAGS;return a?a.web_disable_gel_stp_ecatcher_killswitch:void 0}
;var Xh=[];function Yh(a){Xh.forEach(function(b){return b(a)})}
function Zh(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){$h(b)}}:a}
function $h(a,b,c,d){var e=C("yt.logging.errors.log");e?e(a,"ERROR",b,c,d):(e=P("ERRORS",[]),e.push([a,"ERROR",b,c,d]),Uh("ERRORS",e));Yh(a)}
function ai(a,b,c,d){var e=C("yt.logging.errors.log");e?e(a,"WARNING",b,c,d):(e=P("ERRORS",[]),e.push([a,"WARNING",b,c,d]),Uh("ERRORS",e))}
;var bi=0;B("ytDomDomGetNextId",C("ytDomDomGetNextId")||function(){return++bi});var ci={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function di(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in ci||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function ei(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
di.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
di.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
di.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var kb=z.ytEventsEventsListeners||{};B("ytEventsEventsListeners",kb);var fi=z.ytEventsEventsCounter||{count:0};B("ytEventsEventsCounter",fi);
function gi(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return jb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Pa(e[4])&&Pa(d)&&lb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
function hi(a){a&&("string"==typeof a&&(a=[a]),E(a,function(b){if(b in kb){var c=kb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?ii()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete kb[b]}}))}
var ii=ab(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function ji(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=gi(a,b,c,d);if(e)return e;e=++fi.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new di(h);if(!Id(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new di(h);
h.currentTarget=a;return c.call(a,h)};
g=Zh(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),ii()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);kb[e]=[a,b,c,g,d];return e}
;function ki(a,b){"function"===typeof a&&(a=Zh(a));return window.setTimeout(a,b)}
function li(a,b){"function"===typeof a&&(a=Zh(a));return window.setInterval(a,b)}
;var mi=/^[\w.]*$/,ni={q:!0,search_query:!0};function oi(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1==f.length&&f[0]||2==f.length)try{var g=pi(f[0]||""),h=pi(f[1]||"");g in c?Array.isArray(c[g])?hb(c[g],h):c[g]=[c[g],h]:c[g]=h}catch(n){var k=n,l=f[0],m=String(oi);k.args=[{key:l,value:f[1],query:a,method:qi==m?"unchanged":m}];ni.hasOwnProperty(l)||ai(k)}}return c}
var qi=String(oi);function ri(a){var b=[];ib(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];E(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function si(a){"?"==a.charAt(0)&&(a=a.substr(1));return oi(a,"&")}
function ti(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=si(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);b=a;a=Tb(e);a?(c=b.indexOf("#"),0>c&&(c=b.length),f=b.indexOf("?"),0>f||f>c?(f=c,e=""):e=b.substring(f+1,c),b=[b.slice(0,f),e,b.slice(c)],c=b[1],b[1]=a?c?c+"&"+a:a:c,a=b[0]+(b[1]?"?"+b[1]:"")+b[2]):a=b;return a+d}
function ui(a){if(!b)var b=window.location.href;var c=a.match(Ob)[1]||null,d=Qb(a);c&&d?(a=a.match(Ob),b=b.match(Ob),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?Qb(b)==d&&(Number(b.match(Ob)[4]||null)||null)==(Number(a.match(Ob)[4]||null)||null):!0;return a}
function pi(a){return a&&a.match(mi)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function R(a){a=vi(a);return"string"===typeof a&&"false"===a?!1:!!a}
function wi(a,b){a=vi(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function vi(a){var b=P("EXPERIMENTS_FORCED_FLAGS",{})||{};return void 0!==b[a]?b[a]:P("EXPERIMENT_FLAGS",{})[a]}
function xi(){for(var a=[],b=P("EXPERIMENTS_FORCED_FLAGS",{}),c=u(Object.keys(b)),d=c.next();!d.done;d=c.next())d=d.value,a.push({key:d,value:String(b[d])});c=P("EXPERIMENT_FLAGS",{});var e=u(Object.keys(c));for(d=e.next();!d.done;d=e.next())d=d.value,d.startsWith("force_")&&void 0===b[d]&&a.push({key:d,value:String(c[d])});return a}
;function yi(a){var b=zi;a=void 0===a?C("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=ce;e.flash="0";a:{try{var f=b.h.top.location.href}catch(W){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);try{e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?Ed:g;try{var h=g.history.length}catch(W){h=0}e.u_his=h;var k;e.u_h=null==(k=Ed.screen)?void 0:k.height;var l;e.u_w=null==(l=Ed.screen)?void 0:l.width;var m;e.u_ah=null==(m=Ed.screen)?void 0:m.availHeight;var n;e.u_aw=null==
(n=Ed.screen)?void 0:n.availWidth;var r;e.u_cd=null==(r=Ed.screen)?void 0:r.colorDepth}catch(W){}h=b.h;try{var q=h.screenX;var y=h.screenY}catch(W){}try{var A=h.outerWidth;var H=h.outerHeight}catch(W){}try{var K=h.innerWidth;var M=h.innerHeight}catch(W){}try{var O=h.screenLeft;var pb=h.screenTop}catch(W){}try{K=h.innerWidth,M=h.innerHeight}catch(W){}try{var uc=h.screen.availWidth;var Aa=h.screen.availTop}catch(W){}q=[O,pb,q,y,uc,Aa,A,H,K,M];y=b.h.top;try{var ra=(y||window).document,X="CSS1Compat"==
ra.compatMode?ra.documentElement:ra.body;var ba=(new Gd(X.clientWidth,X.clientHeight)).round()}catch(W){ba=new Gd(-12245933,-12245933)}ra=ba;ba={};var ca=void 0===ca?z:ca;X=new Xe;ca.SVGElement&&ca.document.createElementNS&&X.set(0);y=ae();y["allow-top-navigation-by-user-activation"]&&X.set(1);y["allow-popups-to-escape-sandbox"]&&X.set(2);ca.crypto&&ca.crypto.subtle&&X.set(3);ca.TextDecoder&&ca.TextEncoder&&X.set(4);ca=Ye(X);ba.bc=ca;ba.bih=ra.height;ba.biw=ra.width;ba.brdim=q.join();b=b.i;b=(ba.vis=
b.prerendering?3:{visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,ba.wgl=!!Ed.WebGLRenderingContext,ba);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var zi=new function(){var a=window.document;this.h=window;this.i=a};
B("yt.ads_.signals_.getAdSignalsString",function(a){return ri(yi(a))});Date.now();var Ai="XMLHttpRequest"in z?function(){return new XMLHttpRequest}:null;
function Bi(){if(!Ai)return null;var a=Ai();return"open"in a?a:null}
;var Ci={Authorization:"AUTHORIZATION","X-Goog-EOM-Visitor-Id":"EOM_VISITOR_DATA","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL",
"X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Di="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" ").concat(ia(ee)),Ei=!1;
function Fi(a,b){b=void 0===b?{}:b;var c=ui(a),d=R("web_ajax_ignore_global_headers_if_set"),e;for(e in Ci){var f=P(Ci[e]);"X-Goog-Visitor-Id"!==e||f||(f=P("VISITOR_DATA"));!f||!c&&Qb(a)||d&&void 0!==b[e]||(b[e]=f)}"X-Goog-EOM-Visitor-Id"in b&&"X-Goog-Visitor-Id"in b&&delete b["X-Goog-Visitor-Id"];if(c||!Qb(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!Qb(a)){try{var g=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(h){}g&&(b["X-YouTube-Time-Zone"]=g)}document.location.hostname.endsWith("youtubeeducation.com")||
!c&&Qb(a)||(b["X-YouTube-Ad-Signals"]=ri(yi()));return b}
function Gi(a){var b=window.location.search,c=Qb(a);R("debug_handle_relative_url_for_query_forward_killswitch")||!c&&ui(a)&&(c=document.location.hostname);var d=Pb(a.match(Ob)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=si(b),f={};E(Di,function(g){e[g]&&(f[g]=e[g])});
return ti(a,f||{},!1)}
function Hi(a,b){var c=b.format||"JSON";a=Ii(a,b);var d=Ji(a,b),e=!1,f=Ki(a,function(k){if(!e){e=!0;h&&window.clearTimeout(h);a:switch(k&&"status"in k?k.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:var l=!0;break a;default:l=!1}var m=null,n=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||n||r)m=Li(a,c,k,b.convertToSafeHtml);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(m&&m.return_code,10);break a;case "RAW":l=!0;break a}l=
!!m}m=m||{};n=b.context||z;l?b.onSuccess&&b.onSuccess.call(n,k,m):b.onError&&b.onError.call(n,k,m);b.onFinish&&b.onFinish.call(n,k,m)}},b.method,d,b.headers,b.responseType,b.withCredentials);
d=b.timeout||0;if(b.onTimeout&&0<d){var g=b.onTimeout;var h=ki(function(){e||(e=!0,f.abort(),window.clearTimeout(h),g.call(b.context||z,f))},d)}}
function Ii(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=P("XSRF_FIELD_NAME");if(b=b.urlParams)b[c]&&delete b[c],a=ti(a,b||{},!0);return a}
function Ji(a,b){var c=P("XSRF_FIELD_NAME"),d=P("XSRF_TOKEN"),e=b.postBody||"",f=b.postParams,g=P("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||Qb(a)&&!b.withCredentials&&Qb(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);(R("ajax_parse_query_data_only_when_filled")&&f&&0<Object.keys(f).length||f)&&"string"===typeof e&&(e=si(e),ob(e,f),e=b.postBodyFormat&&"JSON"==b.postBodyFormat?
JSON.stringify(e):Tb(e));if(!(a=e)&&(a=f)){a:{for(var k in f){f=!1;break a}f=!0}a=!f}!Ei&&a&&"POST"!=b.method&&(Ei=!0,$h(Error("AJAX request with postData should use POST")));return e}
function Li(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,ai(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Mi(a):null)e={},E(a.getElementsByTagName("*"),function(g){e[g.tagName]=Ni(g)})}d&&Oi(e);
return e}
function Oi(a){if(Pa(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;sb("HTML that is escaped and sanitized server-side and passed through yt.net.ajax");var d=a[b];if(void 0===qb){var e=null;var f=z.trustedTypes;if(f&&f.createPolicy){try{e=f.createPolicy("goog#html",{createHTML:Wa,createScript:Wa,createScriptURL:Wa})}catch(g){z.console&&z.console.error(g.message)}qb=e}else qb=e}d=(e=qb)?e.createHTML(d):d;a[c]=new Nb(d)}else Oi(a[b])}}
function Mi(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ni(a){var b="";E(a.childNodes,function(c){b+=c.nodeValue});
return b}
function Ki(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Zh(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=Bi();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;R("debug_forward_web_query_parameters")&&(a=Gi(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Fi(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;function Pi(){if(!z.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return z.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":z.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":z.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":z.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;B("ytglobal.prefsUserPrefsPrefs_",C("ytglobal.prefsUserPrefsPrefs_")||{});var Qi={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},Ri={CONN_DEFAULT:0,CONN_UNKNOWN:1,CONN_NONE:2,CONN_WIFI:3,CONN_CELLULAR_2G:4,CONN_CELLULAR_3G:5,CONN_CELLULAR_4G:6,CONN_CELLULAR_UNKNOWN:7,CONN_DISCO:8,CONN_CELLULAR_5G:9,CONN_WIFI_METERED:10,CONN_CELLULAR_5G_SA:11,
CONN_CELLULAR_5G_NSA:12,CONN_INVALID:31},Si={EFFECTIVE_CONNECTION_TYPE_UNKNOWN:0,EFFECTIVE_CONNECTION_TYPE_OFFLINE:1,EFFECTIVE_CONNECTION_TYPE_SLOW_2G:2,EFFECTIVE_CONNECTION_TYPE_2G:3,EFFECTIVE_CONNECTION_TYPE_3G:4,EFFECTIVE_CONNECTION_TYPE_4G:5},Ti={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};function Ui(){var a=z.navigator;return a?a.connection:void 0}
;function Vi(){}
function Wi(a,b){return Xi(a,0,b)}
Vi.prototype.L=function(a,b){return Xi(a,1,b)};
function Yi(a,b){Xi(a,2,b)}
;function Zi(){Vi.apply(this,arguments)}
v(Zi,Vi);function $i(){Zi.h||(Zi.h=new Zi);return Zi.h}
function Xi(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=C("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):ki(a,c||0)}
Zi.prototype.Z=function(a){if(void 0===a||!Number.isNaN(Number(a))){var b=C("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}};
Zi.prototype.start=function(){var a=C("yt.scheduler.instance.start");a&&a()};
var We=$i();function aj(a){var b=Ia.apply(1,arguments);var c=Error.call(this,a);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.args=[].concat(ia(b))}
v(aj,Error);function bj(){try{return cj(),!0}catch(a){return!1}}
function cj(){if(void 0!==P("DATASYNC_ID"))return P("DATASYNC_ID");throw new aj("Datasync ID not set","unknown");}
;var dj=qc||rc;function ej(a){var b=new Ug;if(b.h)try{b.h.setItem("__sak","1");b.h.removeItem("__sak");var c=!0}catch(d){c=!1}else c=!1;(b=c?a?new $g(b,a):b:null)||(a=new Vg(a||"UserDataSharedStore"),b=a.h?a:null);this.h=(a=b)?new Qg(a):null;this.i=document.domain||window.location.hostname}
ej.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Vf(b))}catch(f){return}else e=escape(b);b=this.i;le.set(""+a,e,{Ka:c,path:"/",domain:void 0===b?"youtube.com":b,secure:!1})};
ej.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=le.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
ej.prototype.remove=function(a){this.h&&this.h.remove(a);var b=this.i;le.remove(""+a,"/",void 0===b?"youtube.com":b)};var fj=function(){var a;return function(){a||(a=new ej("ytidb"));return a}}();
function gj(){var a;return null==(a=fj())?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
;var hj=[],ij=!1;function jj(a){ij||(hj.push({type:"ERROR",payload:a}),10<hj.length&&hj.shift())}
function kj(a,b){ij||(hj.push({type:"EVENT",eventType:a,payload:b}),10<hj.length&&hj.shift())}
;function lj(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function mj(a){return a.substr(0,a.indexOf(":"))||a}
;var nj={},oj=(nj.AUTH_INVALID="No user identifier specified.",nj.EXPLICIT_ABORT="Transaction was explicitly aborted.",nj.IDB_NOT_SUPPORTED="IndexedDB is not supported.",nj.MISSING_INDEX="Index not created.",nj.MISSING_OBJECT_STORES="Object stores not created.",nj.DB_DELETED_BY_MISSING_OBJECT_STORES="Database is deleted because expected object stores were not created.",nj.DB_REOPENED_BY_MISSING_OBJECT_STORES="Database is reopened because expected object stores were not created.",nj.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",
nj.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",nj.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",nj.EXECUTE_TRANSACTION_ON_CLOSED_DB="Can't start a transaction on a closed database",nj.INCOMPATIBLE_DB_VERSION="The binary is incompatible with the database version",nj),pj={},qj=(pj.AUTH_INVALID="ERROR",pj.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",pj.EXPLICIT_ABORT="IGNORED",pj.IDB_NOT_SUPPORTED="ERROR",pj.MISSING_INDEX=
"WARNING",pj.MISSING_OBJECT_STORES="ERROR",pj.DB_DELETED_BY_MISSING_OBJECT_STORES="WARNING",pj.DB_REOPENED_BY_MISSING_OBJECT_STORES="WARNING",pj.QUOTA_EXCEEDED="WARNING",pj.QUOTA_MAYBE_EXCEEDED="WARNING",pj.UNKNOWN_ABORT="WARNING",pj.INCOMPATIBLE_DB_VERSION="WARNING",pj),rj={},sj=(rj.AUTH_INVALID=!1,rj.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,rj.EXPLICIT_ABORT=!1,rj.IDB_NOT_SUPPORTED=!1,rj.MISSING_INDEX=!1,rj.MISSING_OBJECT_STORES=!1,rj.DB_DELETED_BY_MISSING_OBJECT_STORES=!1,rj.DB_REOPENED_BY_MISSING_OBJECT_STORES=
!1,rj.QUOTA_EXCEEDED=!1,rj.QUOTA_MAYBE_EXCEEDED=!0,rj.UNKNOWN_ABORT=!0,rj.INCOMPATIBLE_DB_VERSION=!1,rj);function T(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?oj[a]:c;d=void 0===d?qj[a]:d;e=void 0===e?sj[a]:e;aj.call(this,c,Object.assign({},{name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,T.prototype)}
v(T,aj);function tj(a,b){T.call(this,"MISSING_OBJECT_STORES",{expectedObjectStores:b,foundObjectStores:a},oj.MISSING_OBJECT_STORES);Object.setPrototypeOf(this,tj.prototype)}
v(tj,T);function uj(a,b){var c=Error.call(this);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.index=a;this.objectStore=b;Object.setPrototypeOf(this,uj.prototype)}
v(uj,Error);var vj=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function wj(a,b,c,d){b=mj(b);var e=a instanceof Error?a:Error("Unexpected error: "+a);if(e instanceof T)return e;a={objectStoreNames:c,dbName:b,dbVersion:d};if("QuotaExceededError"===e.name)return new T("QUOTA_EXCEEDED",a);if(sc&&"UnknownError"===e.name)return new T("QUOTA_MAYBE_EXCEEDED",a);if(e instanceof uj)return new T("MISSING_INDEX",Object.assign({},a,{objectStore:e.objectStore,index:e.index}));if("InvalidStateError"===e.name&&vj.some(function(f){return e.message.includes(f)}))return new T("EXECUTE_TRANSACTION_ON_CLOSED_DB",
a);
if("AbortError"===e.name)return new T("UNKNOWN_ABORT",a,e.message);e.args=[Object.assign({},a,{name:"IdbError",jc:e.name})];e.level="WARNING";return e}
function xj(a,b,c){var d=gj();return new T("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c,hasSucceededOnce:null==d?void 0:d.hasSucceededOnce}})}
;function yj(a){if(!a)throw Error();throw a;}
function zj(a){return a}
function Aj(a){this.h=a}
function Bj(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=u(d.i);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=u(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.state={status:"PENDING"};this.h=[];this.i=[];a=a.h;try{a(c,b)}catch(e){b(e)}}
Bj.resolve=function(a){return new Bj(new Aj(function(b,c){a instanceof Bj?a.then(b,c):b(a)}))};
Bj.reject=function(a){return new Bj(new Aj(function(b,c){c(a)}))};
Bj.prototype.then=function(a,b){var c=this,d=null!=a?a:zj,e=null!=b?b:yj;return new Bj(new Aj(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){Cj(c,c,d,f,g)}),c.i.push(function(){Dj(c,c,e,f,g)})):"FULFILLED"===c.state.status?Cj(c,c,d,f,g):"REJECTED"===c.state.status&&Dj(c,c,e,f,g)}))};
function Ej(a,b){a.then(void 0,b)}
function Cj(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof Bj?Fj(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Dj(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof Bj?Fj(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Fj(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof Bj?Fj(a,b,f,d,e):d(f)},function(f){e(f)})}
;function Gj(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function Hj(a){return new Promise(function(b,c){Gj(a,b,c)})}
function Ij(a){return new Bj(new Aj(function(b,c){Gj(a,b,c)}))}
;function Jj(a,b){return new Bj(new Aj(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()}))}
;var Kj=window,U=Kj.ytcsi&&Kj.ytcsi.now?Kj.ytcsi.now:Kj.performance&&Kj.performance.timing&&Kj.performance.now&&Kj.performance.timing.navigationStart?function(){return Kj.performance.timing.navigationStart+Kj.performance.now()}:function(){return(new Date).getTime()};function Lj(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(U());this.i=!1}
p=Lj.prototype;p.add=function(a,b,c){return Mj(this,[a],{mode:"readwrite",H:!0},function(d){return d.objectStore(a).add(b,c)})};
p.clear=function(a){return Mj(this,[a],{mode:"readwrite",H:!0},function(b){return b.objectStore(a).clear()})};
p.close=function(){this.h.close();var a;(null==(a=this.options)?0:a.closed)&&this.options.closed()};
function Nj(a,b,c){a=a.h.createObjectStore(b,c);return new Oj(a)}
p.delete=function(a,b){return Mj(this,[a],{mode:"readwrite",H:!0},function(c){return c.objectStore(a).delete(b)})};
p.get=function(a,b){return Mj(this,[a],{mode:"readonly",H:!0},function(c){return c.objectStore(a).get(b)})};
function Pj(a,b,c){return Mj(a,[b],{mode:"readwrite",H:!0},function(d){d=d.objectStore(b);return Ij(d.h.put(c,void 0))})}
p.objectStoreNames=function(){return Array.from(this.h.objectStoreNames)};
function Mj(a,b,c,d){var e,f,g,h,k,l,m,n,r,q,y,A;return x(function(H){switch(H.h){case 1:var K={mode:"readonly",H:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};"string"===typeof c?K.mode=c:Object.assign(K,c);e=K;a.transactionCount++;f=e.H?3:1;g=0;case 2:if(h){H.s(3);break}g++;k=Math.round(U());wa(H,4);l=a.h.transaction(b,e.mode);K=new Qj(l);K=Rj(K,d);return w(H,K,6);case 6:return m=H.i,n=Math.round(U()),Sj(a,k,n,g,void 0,b.join(),e),H.return(m);case 4:r=ya(H);q=Math.round(U());y=wj(r,a.h.name,b.join(),a.h.version);
if((A=y instanceof T&&!y.h)||g>=f)Sj(a,k,q,g,y,b.join(),e),h=y;H.s(2);break;case 3:return H.return(Promise.reject(h))}})}
function Sj(a,b,c,d,e,f,g){b=c-b;e?(e instanceof T&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&kj("QUOTA_EXCEEDED",{dbName:mj(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof T&&"UNKNOWN_ABORT"===e.type&&(c-=a.j,0>c&&c>=Math.pow(2,31)&&(c=0),kj("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),Tj(a,!1,d,f,b,g.tag),jj(e)):Tj(a,!0,d,f,b,g.tag)}
function Tj(a,b,c,d,e,f){kj("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:void 0===f?"IDB_TRANSACTION_TAG_UNKNOWN":f})}
p.getName=function(){return this.h.name};
function Oj(a){this.h=a}
p=Oj.prototype;p.add=function(a,b){return Ij(this.h.add(a,b))};
p.autoIncrement=function(){return this.h.autoIncrement};
p.clear=function(){return Ij(this.h.clear()).then(function(){})};
function Uj(a,b,c){a.h.createIndex(b,c,{unique:!1})}
function Vj(a,b){return Wj(a,{query:b},function(c){return c.delete().then(function(){return c.continue()})}).then(function(){})}
p.delete=function(a){return a instanceof IDBKeyRange?Vj(this,a):Ij(this.h.delete(a))};
p.get=function(a){return Ij(this.h.get(a))};
p.index=function(a){try{return new Xj(this.h.index(a))}catch(b){if(b instanceof Error&&"NotFoundError"===b.name)throw new uj(a,this.h.name);throw b;}};
p.getName=function(){return this.h.name};
p.keyPath=function(){return this.h.keyPath};
function Wj(a,b,c){a=a.h.openCursor(b.query,b.direction);return Yj(a).then(function(d){return Jj(d,c)})}
function Qj(a){var b=this;this.h=a;this.j=new Map;this.i=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.i){e=T;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function Rj(a,b){var c=new Promise(function(d,e){try{Ej(b(a).then(function(f){d(f)}),e)}catch(f){e(f),a.abort()}});
return Promise.all([c,a.done]).then(function(d){return u(d).next().value})}
Qj.prototype.abort=function(){this.h.abort();this.i=!0;throw new T("EXPLICIT_ABORT");};
Qj.prototype.objectStore=function(a){a=this.h.objectStore(a);var b=this.j.get(a);b||(b=new Oj(a),this.j.set(a,b));return b};
function Xj(a){this.h=a}
p=Xj.prototype;p.delete=function(a){return Nk(this,{query:a},function(b){return b.delete().then(function(){return b.continue()})})};
p.get=function(a){return Ij(this.h.get(a))};
p.getKey=function(a){return Ij(this.h.getKey(a))};
p.keyPath=function(){return this.h.keyPath};
p.unique=function(){return this.h.unique};
function Nk(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return Yj(a).then(function(d){return Jj(d,c)})}
function Ok(a,b){this.request=a;this.cursor=b}
function Yj(a){return Ij(a).then(function(b){return b?new Ok(a,b):null})}
p=Ok.prototype;p.advance=function(a){this.cursor.advance(a);return Yj(this.request)};
p.continue=function(a){this.cursor.continue(a);return Yj(this.request)};
p.delete=function(){return Ij(this.cursor.delete()).then(function(){})};
p.getKey=function(){return this.cursor.key};
p.S=function(){return this.cursor.value};
p.update=function(a){return Ij(this.cursor.update(a))};function Pk(a,b,c){return new Promise(function(d,e){function f(){r||(r=new Lj(g.result,{closed:n}));return r}
var g=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var h=c.lb,k=c.mb,l=c.Fb,m=c.upgrade,n=c.closed,r;g.addEventListener("upgradeneeded",function(q){try{if(null===q.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===g.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");q.dataLoss&&"none"!==q.dataLoss&&kj("IDB_DATA_CORRUPTED",{reason:q.dataLossMessage||"unknown reason",dbName:mj(a)});var y=f(),A=new Qj(g.transaction);m&&
m(y,function(H){return q.oldVersion<H&&q.newVersion>=H},A);
A.done.catch(function(H){e(H)})}catch(H){e(H)}});
g.addEventListener("success",function(){var q=g.result;k&&q.addEventListener("versionchange",function(){k(f())});
q.addEventListener("close",function(){kj("IDB_UNEXPECTEDLY_CLOSED",{dbName:mj(a),dbVersion:q.version});l&&l()});
d(f())});
g.addEventListener("error",function(){e(g.error)});
h&&g.addEventListener("blocked",function(){h()})})}
function Qk(a,b,c){c=void 0===c?{}:c;return Pk(a,b,c)}
function Rk(a,b){b=void 0===b?{}:b;var c,d,e,f;return x(function(g){if(1==g.h)return wa(g,2),c=self.indexedDB.deleteDatabase(a),d=b,(e=d.lb)&&c.addEventListener("blocked",function(){e()}),w(g,Hj(c),4);
if(2!=g.h)return xa(g,0);f=ya(g);throw wj(f,a,"",-1);})}
;function Sk(a){return new Promise(function(b){Yi(function(){b()},a)})}
function Tk(a,b){this.name=a;this.options=b;this.l=!0;this.m=this.o=0;this.i=500}
Tk.prototype.j=function(a,b,c){c=void 0===c?{}:c;return Qk(a,b,c)};
Tk.prototype.delete=function(a){a=void 0===a?{}:a;return Rk(this.name,a)};
function Uk(a,b){return new T("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
function Vk(a,b){if(!b)throw xj("openWithToken",mj(a.name));return Wk(a)}
function Wk(a){function b(){var f,g,h,k,l,m,n,r,q,y;return x(function(A){switch(A.h){case 1:return g=null!=(f=Error().stack)?f:"",wa(A,2),w(A,a.j(a.name,a.options.version,d),4);case 4:h=A.i;for(var H=a.options,K=[],M=u(Object.keys(H.da)),O=M.next();!O.done;O=M.next()){O=O.value;var pb=H.da[O],uc=void 0===pb.Db?Number.MAX_VALUE:pb.Db;!(h.h.version>=pb.ga)||h.h.version>=uc||h.h.objectStoreNames.contains(O)||K.push(O)}k=K;if(0===k.length){A.s(5);break}l=Object.keys(a.options.da);m=h.objectStoreNames();
if(a.m<wi("ytidb_reopen_db_retries",0))return a.m++,h.close(),jj(new T("DB_REOPENED_BY_MISSING_OBJECT_STORES",{dbName:a.name,expectedObjectStores:l,foundObjectStores:m})),A.return(b());if(!(a.o<wi("ytidb_remake_db_retries",1))){A.s(6);break}a.o++;if(!R("ytidb_remake_db_enable_backoff_delay")){A.s(7);break}return w(A,Sk(a.i),8);case 8:a.i*=2;case 7:return w(A,a.delete(),9);case 9:return jj(new T("DB_DELETED_BY_MISSING_OBJECT_STORES",{dbName:a.name,expectedObjectStores:l,foundObjectStores:m})),A.return(b());
case 6:throw new tj(m,l);case 5:return A.return(h);case 2:n=ya(A);if(n instanceof DOMException?"VersionError"!==n.name:"DOMError"in self&&n instanceof DOMError?"VersionError"!==n.name:!(n instanceof Object&&"message"in n)||"An attempt was made to open a database using a lower version than the existing version."!==n.message){A.s(10);break}return w(A,a.j(a.name,void 0,Object.assign({},d,{upgrade:void 0})),11);case 11:r=A.i;q=r.h.version;if(void 0!==a.options.version&&q>a.options.version+1)throw r.close(),
a.l=!1,Uk(a,q);return A.return(r);case 10:throw c(),n instanceof Error&&!R("ytidb_async_stack_killswitch")&&(n.stack=n.stack+"\n"+g.substring(g.indexOf("\n")+1)),wj(n,a.name,"",null!=(y=a.options.version)?y:-1);}})}
function c(){a.h===e&&(a.h=void 0)}
if(!a.l)throw Uk(a);if(a.h)return a.h;var d={mb:function(f){f.close()},
closed:c,Fb:c,upgrade:a.options.upgrade};var e=b();a.h=e;return a.h}
;var Xk=new Tk("YtIdbMeta",{da:{databases:{ga:1}},upgrade:function(a,b){b(1)&&Nj(a,"databases",{keyPath:"actualName"})}});
function Yk(a,b){var c;return x(function(d){if(1==d.h)return w(d,Vk(Xk,b),2);c=d.i;return d.return(Mj(c,["databases"],{H:!0,mode:"readwrite"},function(e){var f=e.objectStore("databases");return f.get(a.actualName).then(function(g){if(g?a.actualName!==g.actualName||a.publicName!==g.publicName||a.userIdentifier!==g.userIdentifier:1)return Ij(f.h.put(a,void 0)).then(function(){})})}))})}
function Zk(a,b){var c;return x(function(d){if(1==d.h)return a?w(d,Vk(Xk,b),2):d.return();c=d.i;return d.return(c.delete("databases",a))})}
function $k(a,b){var c,d;return x(function(e){return 1==e.h?(c=[],w(e,Vk(Xk,b),2)):3!=e.h?(d=e.i,w(e,Mj(d,["databases"],{H:!0,mode:"readonly"},function(f){c.length=0;return Wj(f.objectStore("databases"),{},function(g){a(g.S())&&c.push(g.S());return g.continue()})}),3)):e.return(c)})}
function al(a){return $k(function(b){return"LogsDatabaseV2"===b.publicName&&void 0!==b.userIdentifier},a)}
;var bl,cl=new function(){}(new function(){});
function dl(){var a,b,c,d;return x(function(e){switch(e.h){case 1:a=gj();if(null==(b=a)?0:b.hasSucceededOnce)return e.return(!0);var f;if(f=dj)f=/WebKit\/([0-9]+)/.exec(Kb()),f=!!(f&&600<=parseInt(f[1],10));f&&(f=/WebKit\/([0-9]+)/.exec(Kb()),f=!(f&&602<=parseInt(f[1],10)));if(f||ec)return e.return(!1);try{if(c=self,!(c.indexedDB&&c.IDBIndex&&c.IDBKeyRange&&c.IDBObjectStore))return e.return(!1)}catch(g){return e.return(!1)}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return e.return(!1);
wa(e,2);d={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return w(e,Yk(d,cl),4);case 4:return w(e,Zk("yt-idb-test-do-not-use",cl),5);case 5:return e.return(!0);case 2:return ya(e),e.return(!1)}})}
function el(){if(void 0!==bl)return bl;ij=!0;return bl=dl().then(function(a){ij=!1;var b;if(null!=(b=fj())&&b.h){var c;b={hasSucceededOnce:(null==(c=gj())?void 0:c.hasSucceededOnce)||a};var d;null==(d=fj())||d.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0)}return a})}
function fl(){return C("ytglobal.idbToken_")||void 0}
function gl(){var a=fl();return a?Promise.resolve(a):el().then(function(b){(b=b?cl:void 0)&&B("ytglobal.idbToken_",b);return b})}
;new Wf;function hl(a){if(!bj())throw a=new T("AUTH_INVALID",{dbName:a}),jj(a),a;var b=cj();return{actualName:a+":"+b,publicName:a,userIdentifier:b}}
function il(a,b,c,d){var e,f,g,h,k,l;return x(function(m){switch(m.h){case 1:return f=null!=(e=Error().stack)?e:"",w(m,gl(),2);case 2:g=m.i;if(!g)throw h=xj("openDbImpl",a,b),R("ytidb_async_stack_killswitch")||(h.stack=h.stack+"\n"+f.substring(f.indexOf("\n")+1)),jj(h),h;lj(a);k=c?{actualName:a,publicName:a,userIdentifier:void 0}:hl(a);wa(m,3);return w(m,Yk(k,g),5);case 5:return w(m,Qk(k.actualName,b,d),6);case 6:return m.return(m.i);case 3:return l=ya(m),wa(m,7),w(m,Zk(k.actualName,g),9);case 9:xa(m,
8);break;case 7:ya(m);case 8:throw l;}})}
function jl(a,b,c){c=void 0===c?{}:c;return il(a,b,!1,c)}
function kl(a,b,c){c=void 0===c?{}:c;return il(a,b,!0,c)}
function ll(a,b){b=void 0===b?{}:b;var c,d;return x(function(e){if(1==e.h)return w(e,gl(),2);if(3!=e.h){c=e.i;if(!c)return e.return();lj(a);d=hl(a);return w(e,Rk(d.actualName,b),3)}return w(e,Zk(d.actualName,c),0)})}
function ml(a,b,c){a=a.map(function(d){return x(function(e){return 1==e.h?w(e,Rk(d.actualName,b),2):w(e,Zk(d.actualName,c),0)})});
return Promise.all(a).then(function(){})}
function nl(){var a=void 0===a?{}:a;var b,c;return x(function(d){if(1==d.h)return w(d,gl(),2);if(3!=d.h){b=d.i;if(!b)return d.return();lj("LogsDatabaseV2");return w(d,al(b),3)}c=d.i;return w(d,ml(c,a,b),0)})}
function ol(a,b){b=void 0===b?{}:b;var c;return x(function(d){if(1==d.h)return w(d,gl(),2);if(3!=d.h){c=d.i;if(!c)return d.return();lj(a);return w(d,Rk(a,b),3)}return w(d,Zk(a,c),0)})}
;function pl(a,b){Tk.call(this,a,b);this.options=b;lj(a)}
v(pl,Tk);function ql(a,b){var c;return function(){c||(c=new pl(a,b));return c}}
pl.prototype.j=function(a,b,c){c=void 0===c?{}:c;return(this.options.Fa?kl:jl)(a,b,Object.assign({},c))};
pl.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.Fa?ol:ll)(this.name,a)};
function rl(a,b){return ql(a,b)}
;var sl={},tl=rl("ytGcfConfig",{da:(sl.coldConfigStore={ga:1},sl.hotConfigStore={ga:1},sl),Fa:!1,upgrade:function(a,b){b(1)&&(Uj(Nj(a,"hotConfigStore",{keyPath:"key",autoIncrement:!0}),"hotTimestampIndex","timestamp"),Uj(Nj(a,"coldConfigStore",{keyPath:"key",autoIncrement:!0}),"coldTimestampIndex","timestamp"))},
version:1});function ul(a){return Vk(tl(),a)}
function vl(a,b,c){var d,e,f;return x(function(g){switch(g.h){case 1:return d={config:a,hashData:b,timestamp:U()},w(g,ul(c),2);case 2:return e=g.i,w(g,e.clear("hotConfigStore"),3);case 3:return w(g,Pj(e,"hotConfigStore",d),4);case 4:return f=g.i,g.return(f)}})}
function wl(a,b,c,d){var e,f,g;return x(function(h){switch(h.h){case 1:return e={config:a,hashData:b,configData:c,timestamp:U()},w(h,ul(d),2);case 2:return f=h.i,w(h,f.clear("coldConfigStore"),3);case 3:return w(h,Pj(f,"coldConfigStore",e),4);case 4:return g=h.i,h.return(g)}})}
;function xl(){}
function yl(a,b,c){var d,e;return x(function(f){if(!R("gcf_config_store_update_enabled"))return f.s(0);a.h=b;B("yt.gcf.config.hotConfigGroup",a.h);a.hotHashData=c;B("yt.gcf.config.hotHashData",a.hotHashData);d=fl();return d?w(f,vl(b,c,d),0):(e=xj("updateHotConfig token error"),ai(e),f.s(0))})}
function zl(a,b,c){var d,e;return x(function(f){if(!R("gcf_config_store_update_enabled"))return f.s(0);a.coldHashData=c;B("yt.gcf.config.coldHashData",a.coldHashData);d=fl();return d?b.configData?w(f,wl(b,c,b.configData,d),0):f.s(0):(e=xj("updateColdConfig token error"),ai(e),f.s(0))})}
;function Al(){return"INNERTUBE_API_KEY"in Th&&"INNERTUBE_API_VERSION"in Th}
function Bl(){return{ub:P("INNERTUBE_API_KEY"),vb:P("INNERTUBE_API_VERSION"),Ja:P("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),Va:P("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),wb:P("INNERTUBE_CONTEXT_CLIENT_NAME",1),Wa:P("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ya:P("INNERTUBE_CONTEXT_HL"),Xa:P("INNERTUBE_CONTEXT_GL"),xb:P("INNERTUBE_HOST_OVERRIDE")||"",zb:!!P("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),yb:!!P("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",!1),appInstallData:P("SERIALIZED_CLIENT_CONFIG_DATA")}}
function Cl(a){var b={client:{hl:a.Ya,gl:a.Xa,clientName:a.Va,clientVersion:a.Wa,configInfo:a.Ja}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=z.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=P("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=xi();0<c.length&&(b.request={internalExperimentFlags:c});Dl(a,void 0,b);R("enable_third_party_info")&&El(void 0,b);Fl(void 0,b);Gl(a,void 0,b);Hl(void 0,b);R("start_sending_config_hash")&&Il(void 0,
b);P("DELEGATED_SESSION_ID")&&!R("pageid_as_header_web")&&(b.user={onBehalfOfUser:P("DELEGATED_SESSION_ID")});a=Object;c=a.assign;for(var d=b.client,e={},f=u(Object.entries(si(P("DEVICE","")))),g=f.next();!g.done;g=f.next()){var h=u(g.value);g=h.next().value;h=h.next().value;"cbrand"===g?e.deviceMake=h:"cmodel"===g?e.deviceModel=h:"cbr"===g?e.browserName=h:"cbrver"===g?e.browserVersion=h:"cos"===g?e.osName=h:"cosver"===g?e.osVersion=h:"cplatform"===g&&(e.platform=h)}b.client=c.call(a,d,e);return b}
function Jl(a){var b=new sh,c=new jh;I(c,1,a.Ya);I(c,2,a.Xa);I(c,16,a.wb);I(c,17,a.Wa);if(a.Ja){var d=a.Ja,e=new fh;d.coldConfigData&&I(e,1,d.coldConfigData);d.appInstallData&&I(e,6,d.appInstallData);d.coldHashData&&I(e,3,d.coldHashData);d.hotHashData&&I(e,5,d.hotHashData);J(c,fh,62,e)}(d=z.devicePixelRatio)&&1!=d&&I(c,65,d);d=P("EXPERIMENTS_TOKEN","");""!==d&&I(c,54,d);d=xi();if(0<d.length){e=new lh;for(var f=0;f<d.length;f++){var g=new dh;I(g,1,d[f].key);md(g,2,eh,d[f].value);td(e,15,dh,g)}J(b,
lh,5,e)}Dl(a,c);R("enable_third_party_info")&&El(b);Fl(c);Gl(a,c);Hl(c);R("start_sending_config_hash")&&Il(c);P("DELEGATED_SESSION_ID")&&!R("pageid_as_header_web")&&(a=new qh,I(a,3,P("DELEGATED_SESSION_ID")));a=u(Object.entries(si(P("DEVICE",""))));for(d=a.next();!d.done;d=a.next())e=u(d.value),d=e.next().value,e=e.next().value,"cbrand"===d?I(c,12,e):"cmodel"===d?I(c,13,e):"cbr"===d?I(c,87,e):"cbrver"===d?I(c,88,e):"cos"===d?I(c,18,e):"cosver"===d?I(c,19,e):"cplatform"===d&&I(c,42,e);J(b,jh,1,c);
return b}
function Dl(a,b,c){a=a.Va;if("WEB"===a||"MWEB"===a||1===a||2===a)if(b){c=od(b,gh,96)||new gh;var d=Pi();d=Object.keys(uh).indexOf(d);d=-1===d?null:d;null!==d&&I(c,3,d);J(b,gh,96,c)}else c&&(c.client.mainAppWebInfo=null!=(d=c.client.mainAppWebInfo)?d:{},c.client.mainAppWebInfo.webDisplayMode=Pi())}
function El(a,b){var c=C("yt.embedded_player.embed_url");c&&(a?(b=od(a,nh,7)||new nh,I(b,4,c),J(a,nh,7,b)):b&&(b.thirdParty={embedUrl:c}))}
function Fl(a,b){var c;if(R("web_log_memory_total_kbytes")&&(null==(c=z.navigator)?0:c.deviceMemory)){var d;c=null==(d=z.navigator)?void 0:d.deviceMemory;a?I(a,95,1E6*c):b&&(b.client.memoryTotalKbytes=""+1E6*c)}}
function Gl(a,b,c){if(a.appInstallData)if(b){var d;c=null!=(d=od(b,fh,62))?d:new fh;I(c,6,a.appInstallData);J(b,fh,62,c)}else c&&(c.client.configInfo=c.client.configInfo||{},c.client.configInfo.appInstallData=a.appInstallData)}
function Hl(a,b){a:{var c=Ui();if(c){var d=Qi[c.type||"unknown"]||"CONN_UNKNOWN";c=Qi[c.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===d&&"CONN_UNKNOWN"!==c&&(d=c);if("CONN_UNKNOWN"!==d)break a;if("CONN_UNKNOWN"!==c){d=c;break a}}d=void 0}d&&(a?I(a,61,Ri[d]):b&&(b.client.connectionType=d));R("web_log_effective_connection_type")&&(d=Ui(),d=null!=d&&d.effectiveType?Ti.hasOwnProperty(d.effectiveType)?Ti[d.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN":void 0,d&&(a?I(a,94,Si[d]):
b&&(b.client.effectiveConnectionType=d)))}
function Kl(a,b,c){c=void 0===c?{}:c;var d={};P("EOM_VISITOR_DATA")?d={"X-Goog-EOM-Visitor-Id":P("EOM_VISITOR_DATA")}:d={"X-Goog-Visitor-Id":c.visitorData||P("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.cc||P("AUTHORIZATION"))||(a?b="Bearer "+C("gapi.auth.getToken")().ac:b=oe([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=P("SESSION_INDEX",0),R("pageid_as_header_web")&&(d["X-Goog-PageId"]=P("DELEGATED_SESSION_ID")));return d}
function Il(a,b){xl.h||(xl.h=new xl);var c=C("yt.gcf.config.coldConfigData");var d=C("yt.gcf.config.hotHashData");var e=C("yt.gcf.config.coldHashData");if(c&&e&&d)if(a){var f;b=null!=(f=od(a,fh,62))?f:new fh;I(b,1,c);I(b,3,e);I(b,5,d);J(a,fh,62,b)}else b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.coldConfigData=c,b.client.configInfo.coldHashData=e,b.client.configInfo.hotHashData=d)}
;function Ll(a){a=Object.assign({},a);delete a.Authorization;var b=oe();if(b){var c=new Hf;c.update(P("INNERTUBE_API_KEY"));c.update(b);a.hash=wc(c.digest(),3)}return a}
;var Ml;function Nl(){Ml||(Ml=new ej("yt.innertube"));return Ml}
function Ol(a,b,c,d){if(d)return null;d=Nl().get("nextId",!0)||1;var e=Nl().get("requests",!0)||{};e[d]={method:a,request:b,authState:Ll(c),requestTime:Math.round(U())};Nl().set("nextId",d+1,86400,!0);Nl().set("requests",e,86400,!0);return d}
function Pl(a){var b=Nl().get("requests",!0)||{};delete b[a];Nl().set("requests",b,86400,!0)}
function Ql(a){var b=Nl().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(U())-d.requestTime)){var e=d.authState,f=Ll(Kl(!1));lb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(U())),Rl(a,d.method,e,{}));delete b[c]}}Nl().set("requests",b,86400,!0)}}
;function Sl(a){this.sa=this.h=!1;this.potentialEsfErrorCounter=this.i=0;this.handleError=function(){};
this.ca=function(){};
this.now=Date.now;this.ia=!1;var b;this.hb=null!=(b=a.hb)?b:100;var c;this.gb=null!=(c=a.gb)?c:1;var d;this.eb=null!=(d=a.eb)?d:2592E6;var e;this.cb=null!=(e=a.cb)?e:12E4;var f;this.fb=null!=(f=a.fb)?f:5E3;var g;this.A=null!=(g=a.A)?g:void 0;this.xa=!!a.xa;var h;this.wa=null!=(h=a.wa)?h:.1;var k;this.Ca=null!=(k=a.Ca)?k:10;a.handleError&&(this.handleError=a.handleError);a.ca&&(this.ca=a.ca);a.ia&&(this.ia=a.ia);a.sa&&(this.sa=a.sa);this.B=a.B;this.J=a.J;this.D=a.D;this.F=a.F;this.P=a.P;this.Na=a.Na;
this.Ma=a.Ma;Tl(this)&&(!this.B||this.B("networkless_logging"))&&Ul(this)}
function Ul(a){Tl(a)&&!a.ia&&(a.h=!0,a.xa&&Math.random()<=a.wa&&a.D.ob(a.A),Vl(a),a.F.I()&&a.ma(),a.F.X(a.Na,a.ma.bind(a)),a.F.X(a.Ma,a.Qa.bind(a)))}
p=Sl.prototype;p.writeThenSend=function(a,b){var c=this;b=void 0===b?{}:b;if(Tl(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.D.set(d,this.A).then(function(e){d.id=e;c.F.I()&&Wl(c,d)}).catch(function(e){Wl(c,d);
Xl(c,e)})}else this.P(a,b)};
p.sendThenWrite=function(a,b,c){var d=this;b=void 0===b?{}:b;if(Tl(this)&&this.h){var e={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.B&&this.B("nwl_skip_retry")&&(e.skipRetry=c);if(this.F.I()||this.B&&this.B("nwl_aggressive_send_then_write")&&!e.skipRetry){if(!e.skipRetry){var f=b.onError?b.onError:function(){};
b.onError=function(g,h){return x(function(k){if(1==k.h)return w(k,d.D.set(e,d.A).catch(function(l){Xl(d,l)}),2);
f(g,h);k.h=0})}}this.P(a,b,e.skipRetry)}else this.D.set(e,this.A).catch(function(g){d.P(a,b,e.skipRetry);
Xl(d,g)})}else this.P(a,b,this.B&&this.B("nwl_skip_retry")&&c)};
p.sendAndWrite=function(a,b){var c=this;b=void 0===b?{}:b;if(Tl(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0},e=!1,f=b.onSuccess?b.onSuccess:function(){};
d.options.onSuccess=function(g,h){void 0!==d.id?c.D.aa(d.id,c.A):e=!0;c.F.Y&&c.B&&c.B("vss_network_hint")&&c.F.Y(!0);f(g,h)};
this.P(d.url,d.options);this.D.set(d,this.A).then(function(g){d.id=g;e&&c.D.aa(d.id,c.A)}).catch(function(g){Xl(c,g)})}else this.P(a,b)};
p.ma=function(){var a=this;if(!Tl(this))throw xj("throttleSend");this.i||(this.i=this.J.L(function(){var b;return x(function(c){if(1==c.h)return w(c,a.D.Ua("NEW",a.A),2);if(3!=c.h)return b=c.i,b?w(c,Wl(a,b),3):(a.Qa(),c.return());a.i&&(a.i=0,a.ma());c.h=0})},this.hb))};
p.Qa=function(){this.J.Z(this.i);this.i=0};
function Wl(a,b){var c,d;return x(function(e){switch(e.h){case 1:if(!Tl(a))throw c=xj("immediateSend"),c;if(void 0===b.id){e.s(2);break}return w(e,a.D.Bb(b.id,a.A),3);case 3:(d=e.i)?b=d:a.ca(Error("The request cannot be found in the database."));case 2:if(Yl(a,b,a.eb)){e.s(4);break}a.ca(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===b.id){e.s(5);break}return w(e,a.D.aa(b.id,a.A),5);case 5:return e.return();case 4:b.skipRetry||(b=Zl(a,b));if(!b){e.s(0);break}if(!b.skipRetry||
void 0===b.id){e.s(8);break}return w(e,a.D.aa(b.id,a.A),8);case 8:a.P(b.url,b.options,!!b.skipRetry),e.h=0}})}
function Zl(a,b){if(!Tl(a))throw xj("updateRequestHandlers");var c=b.options.onError?b.options.onError:function(){};
b.options.onError=function(e,f){var g,h,k;return x(function(l){switch(l.h){case 1:g=$l(f);if(!(a.B&&a.B("nwl_consider_error_code")&&g||a.B&&!a.B("nwl_consider_error_code")&&a.potentialEsfErrorCounter<=a.Ca)){l.s(2);break}if(!a.F.Ea){l.s(3);break}return w(l,a.F.Ea(),3);case 3:if(a.F.I()){l.s(2);break}c(e,f);if(!a.B||!a.B("nwl_consider_error_code")||void 0===(null==(h=b)?void 0:h.id)){l.s(6);break}return w(l,a.D.Oa(b.id,a.A,!1),6);case 6:return l.return();case 2:if(a.B&&a.B("nwl_consider_error_code")&&
!g&&a.potentialEsfErrorCounter>a.Ca)return l.return();a.potentialEsfErrorCounter++;if(void 0===(null==(k=b)?void 0:k.id)){l.s(8);break}return b.sendCount<a.gb?w(l,a.D.Oa(b.id,a.A),12):w(l,a.D.aa(b.id,a.A),8);case 12:a.J.L(function(){a.F.I()&&a.ma()},a.fb);
case 8:c(e,f),l.h=0}})};
var d=b.options.onSuccess?b.options.onSuccess:function(){};
b.options.onSuccess=function(e,f){var g;return x(function(h){if(1==h.h)return void 0===(null==(g=b)?void 0:g.id)?h.s(2):w(h,a.D.aa(b.id,a.A),2);a.F.Y&&a.B&&a.B("vss_network_hint")&&a.F.Y(!0);d(e,f);h.h=0})};
return b}
function Yl(a,b,c){b=b.timestamp;return a.now()-b>=c?!1:!0}
function Vl(a){if(!Tl(a))throw xj("retryQueuedRequests");a.D.Ua("QUEUED",a.A).then(function(b){b&&!Yl(a,b,a.cb)?a.J.L(function(){return x(function(c){if(1==c.h)return void 0===b.id?c.s(2):w(c,a.D.Oa(b.id,a.A),2);Vl(a);c.h=0})}):a.F.I()&&a.ma()})}
function Xl(a,b){a.ib&&!a.F.I()?a.ib(b):a.handleError(b)}
function Tl(a){return!!a.A||a.sa}
function $l(a){var b;return(a=null==a?void 0:null==(b=a.error)?void 0:b.code)&&400<=a&&599>=a?!1:!0}
;var am=C("ytPubsub2Pubsub2Instance")||new N;N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.na;N.prototype.publish=N.prototype.ea;N.prototype.clear=N.prototype.clear;B("ytPubsub2Pubsub2Instance",am);B("ytPubsub2Pubsub2SubscribedKeys",C("ytPubsub2Pubsub2SubscribedKeys")||{});B("ytPubsub2Pubsub2TopicToKeys",C("ytPubsub2Pubsub2TopicToKeys")||{});B("ytPubsub2Pubsub2IsAsync",C("ytPubsub2Pubsub2IsAsync")||{});B("ytPubsub2Pubsub2SkipSubKey",null);var bm;
function cm(){if(bm)return bm();var a={};bm=rl("LogsDatabaseV2",{da:(a.LogsRequestsStore={ga:2},a),Fa:!1,upgrade:function(b,c,d){c(2)&&Nj(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});c(3);c(5)&&(d=d.objectStore("LogsRequestsStore"),d.h.indexNames.contains("newRequest")&&d.h.deleteIndex("newRequest"),Uj(d,"newRequestV2",["status","interface","timestamp"]));c(7)&&b.h.objectStoreNames.contains("sapisid")&&b.h.deleteObjectStore("sapisid");c(9)&&b.h.objectStoreNames.contains("SWHealthLog")&&b.h.deleteObjectStore("SWHealthLog")},
version:9});return bm()}
;function dm(a){return Vk(cm(),a)}
function em(a,b){var c,d,e,f;return x(function(g){if(1==g.h)return c={startTime:U(),transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},w(g,dm(b),2);if(3!=g.h)return d=g.i,e=Object.assign({},a,{options:JSON.parse(JSON.stringify(a.options)),interface:P("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),w(g,Pj(d,"LogsRequestsStore",e),3);f=g.i;c.Gb=U();fm(c);return g.return(f)})}
function gm(a,b){var c,d,e,f,g,h,k;return x(function(l){if(1==l.h)return c={startTime:U(),transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},w(l,dm(b),2);if(3!=l.h)return d=l.i,e=P("INNERTUBE_CONTEXT_CLIENT_NAME",0),f=[a,e,0],g=[a,e,U()],h=IDBKeyRange.bound(f,g),k=void 0,w(l,Mj(d,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(m){return Nk(m.objectStore("LogsRequestsStore").index("newRequestV2"),{query:h,direction:"prev"},function(n){n.S()&&(k=n.S(),"NEW"===a&&(k.status="QUEUED",n.update(k)))})}),
3);
c.Gb=U();fm(c);return l.return(k)})}
function hm(a,b){var c;return x(function(d){if(1==d.h)return w(d,dm(b),2);c=d.i;return d.return(Mj(c,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(e){var f=e.objectStore("LogsRequestsStore");return f.get(a).then(function(g){if(g)return g.status="QUEUED",Ij(f.h.put(g,void 0)).then(function(){return g})})}))})}
function im(a,b,c){c=void 0===c?!0:c;var d;return x(function(e){if(1==e.h)return w(e,dm(b),2);d=e.i;return e.return(Mj(d,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(f){var g=f.objectStore("LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",c&&(h.sendCount+=1),Ij(g.h.put(h,void 0)).then(function(){return h})):Bj.resolve(void 0)})}))})}
function jm(a,b){var c;return x(function(d){if(1==d.h)return w(d,dm(b),2);c=d.i;return d.return(c.delete("LogsRequestsStore",a))})}
function km(a){var b,c;return x(function(d){if(1==d.h)return w(d,dm(a),2);b=d.i;c=U()-2592E6;return w(d,Mj(b,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(e){return Wj(e.objectStore("LogsRequestsStore"),{},function(f){if(f.S().timestamp<=c)return f.delete().then(function(){return f.continue()})})}),0)})}
function lm(){x(function(a){return w(a,nl(),0)})}
function fm(a){if(!R("nwl_csi_killswitch")&&.01>=Math.random()){var b=C("ytPubsub2Pubsub2Instance");b&&b.publish.call(b,"nwl_transaction_latency_payload".toString(),"nwl_transaction_latency_payload",a)}}
;var mm={},nm=rl("ServiceWorkerLogsDatabase",{da:(mm.SWHealthLog={ga:1},mm),Fa:!0,upgrade:function(a,b){b(1)&&Uj(Nj(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}),"swHealthNewRequest",["interface","timestamp"])},
version:1});function om(a){return Vk(nm(),a)}
function pm(a){var b,c;x(function(d){if(1==d.h)return w(d,om(a),2);b=d.i;c=U()-2592E6;return w(d,Mj(b,["SWHealthLog"],{mode:"readwrite",H:!0},function(e){return Wj(e.objectStore("SWHealthLog"),{},function(f){if(f.S().timestamp<=c)return f.delete().then(function(){return f.continue()})})}),0)})}
function qm(a){var b;return x(function(c){if(1==c.h)return w(c,om(a),2);b=c.i;return w(c,b.clear("SWHealthLog"),0)})}
;var rm={},sm=0;function tm(a){var b=new Image,c=""+sm++;rm[c]=b;b.onload=b.onerror=function(){delete rm[c]};
b.src=a}
;function V(){this.h=new Map;this.i=!1}
function um(){if(!V.h){var a=C("yt.networkRequestMonitor.instance")||new V;B("yt.networkRequestMonitor.instance",a);V.h=a}return V.h}
V.prototype.requestComplete=function(a,b){b&&(this.i=!0);a=this.removeParams(a);this.h.get(a)||this.h.set(a,b)};
V.prototype.isEndpointCFR=function(a){a=this.removeParams(a);return(a=this.h.get(a))?!1:!1===a&&this.i?!0:null};
V.prototype.removeParams=function(a){return a.split("?")[0]};
V.prototype.removeParams=V.prototype.removeParams;V.prototype.isEndpointCFR=V.prototype.isEndpointCFR;V.prototype.requestComplete=V.prototype.requestComplete;V.getInstance=um;var vm;function wm(){vm||(vm=new ej("yt.offline"));return vm}
function xm(a){if(R("offline_error_handling")){var b=wm().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);wm().set("errors",b,2592E3,!0)}}
;function Y(){Pe.call(this);var a=this;this.l=!1;this.i=Ve();this.i.X("networkstatus-online",function(){if(a.l&&R("offline_error_handling")){var b=wm().get("errors",!0);if(b){for(var c in b)if(b[c]){var d=new aj(c,"sent via offline_errors");d.name=b[c].name;d.stack=b[c].stack;d.level=b[c].level;$h(d)}wm().set("errors",{},2592E3,!0)}}})}
v(Y,Pe);function ym(){if(!Y.h){var a=C("yt.networkStatusManager.instance")||new Y;B("yt.networkStatusManager.instance",a);Y.h=a}return Y.h}
p=Y.prototype;p.I=function(){return this.i.I()};
p.Y=function(a){this.i.i=a};
p.tb=function(){var a=window.navigator.onLine;return void 0===a?!0:a};
p.qb=function(){this.l=!0};
p.X=function(a,b){return this.i.X(a,b)};
p.Ea=function(a){a=Te(this.i,a);a.then(function(b){R("use_cfr_monitor")&&um().requestComplete("generate_204",b)});
return a};
Y.prototype.sendNetworkCheckRequest=Y.prototype.Ea;Y.prototype.listen=Y.prototype.X;Y.prototype.enableErrorFlushing=Y.prototype.qb;Y.prototype.getWindowStatus=Y.prototype.tb;Y.prototype.networkStatusHint=Y.prototype.Y;Y.prototype.isNetworkAvailable=Y.prototype.I;Y.getInstance=ym;function zm(a){a=void 0===a?{}:a;Pe.call(this);var b=this;this.i=this.u=0;this.l=ym();var c=C("yt.networkStatusManager.instance.listen").bind(this.l);c&&(a.Da?(this.Da=a.Da,c("networkstatus-online",function(){Am(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){Am(b,"publicytnetworkstatus-offline")})):(c("networkstatus-online",function(){Qe(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){Qe(b,"publicytnetworkstatus-offline")})))}
v(zm,Pe);zm.prototype.I=function(){var a=C("yt.networkStatusManager.instance.isNetworkAvailable");return a?a.bind(this.l)():!0};
zm.prototype.Y=function(a){var b=C("yt.networkStatusManager.instance.networkStatusHint").bind(this.l);b&&b(a)};
zm.prototype.Ea=function(a){var b=this,c;return x(function(d){c=C("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(b.l);return R("skip_network_check_if_cfr")&&um().isEndpointCFR("generate_204")?d.return(new Promise(function(e){var f;b.Y((null==(f=window.navigator)?void 0:f.onLine)||!0);e(b.I())})):c?d.return(c(a)):d.return(!0)})};
function Am(a,b){a.Da?a.i?(We.Z(a.u),a.u=We.L(function(){a.m!==b&&(Qe(a,b),a.m=b,a.i=U())},a.Da-(U()-a.i))):(Qe(a,b),a.m=b,a.i=U()):Qe(a,b)}
;var Bm;function Cm(){var a=Sl.call;Bm||(Bm=new zm({hc:!0,fc:!0}));a.call(Sl,this,{D:{ob:km,aa:jm,Ua:gm,Bb:hm,Oa:im,set:em},F:Bm,handleError:$h,ca:ai,P:Dm,now:U,ib:xm,J:$i(),Na:"publicytnetworkstatus-online",Ma:"publicytnetworkstatus-offline",xa:!0,wa:.1,Ca:wi("potential_esf_error_limit",10),B:R,ia:!(bj()&&"www.youtube-nocookie.com"!==Qb(document.location.toString()))});this.j=new Wf;R("networkless_immediately_drop_all_requests")&&lm();ol("LogsDatabaseV2")}
v(Cm,Sl);function Em(){var a=C("yt.networklessRequestController.instance");a||(a=new Cm,B("yt.networklessRequestController.instance",a),R("networkless_logging")&&gl().then(function(b){a.A=b;Ul(a);a.j.resolve();a.xa&&Math.random()<=a.wa&&a.A&&pm(a.A);R("networkless_immediately_drop_sw_health_store")&&Fm(a)}));
return a}
Cm.prototype.writeThenSend=function(a,b){b||(b={});bj()||(this.h=!1);Sl.prototype.writeThenSend.call(this,a,b)};
Cm.prototype.sendThenWrite=function(a,b,c){b||(b={});bj()||(this.h=!1);Sl.prototype.sendThenWrite.call(this,a,b,c)};
Cm.prototype.sendAndWrite=function(a,b){b||(b={});bj()||(this.h=!1);Sl.prototype.sendAndWrite.call(this,a,b)};
Cm.prototype.awaitInitialization=function(){return this.j.promise};
function Fm(a){var b;x(function(c){if(!a.A)throw b=xj("clearSWHealthLogsDb"),b;return c.return(qm(a.A).catch(function(d){a.handleError(d)}))})}
function Dm(a,b,c){R("use_cfr_monitor")&&Gm(a,b);if(R("use_request_time_ms_header"))b.headers&&(b.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(U())));else{var d;if(null==(d=b.postParams)?0:d.requestTimeMs)b.postParams.requestTimeMs=Math.round(U())}if(c&&0===Object.keys(b).length){var e=void 0===e?"":e;var f=void 0===f?!1:f;if(a)if(e)Ki(a,void 0,"POST",e);else if(P("USE_NET_AJAX_FOR_PING_TRANSPORT",!1))Ki(a,void 0,"GET","",void 0,void 0,f);else{b:{try{var g=new Ya({url:a});if(g.j&&g.i||
g.l){var h=Pb(a.match(Ob)[5]||null);var k=!(!h||!h.endsWith("/aclk")||"1"!==Zb(a,"ri"));break b}}catch(m){}k=!1}if(k){b:{try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,"")){var l=!0;break b}}catch(m){}l=!1}c=l?!0:!1}else c=!1;c||tm(a)}}else Hi(a,b)}
function Gm(a,b){var c=b.onError?b.onError:function(){};
b.onError=function(e,f){um().requestComplete(a,!1);c(e,f)};
var d=b.onSuccess?b.onSuccess:function(){};
b.onSuccess=function(e,f){um().requestComplete(a,!0);d(e,f)}}
;var Hm=z.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:!1};B("ytNetworklessLoggingInitializationOptions",Hm);function Im(a){var b=this;this.config_=null;a?this.config_=a:Al()&&(this.config_=Bl());Wi(function(){Ql(b)},5E3)}
Im.prototype.isReady=function(){!this.config_&&Al()&&(this.config_=Bl());return!!this.config_};
function Rl(a,b,c,d){function e(y){y=void 0===y?!1:y;var A;if(d.retry&&"www.youtube-nocookie.com"!=h&&(y||R("skip_ls_gel_retry")||"application/json"!==g.headers["Content-Type"]||(A=Ol(b,c,l,k)),A)){var H=g.onSuccess,K=g.onFetchSuccess;g.onSuccess=function(M,O){Pl(A);H(M,O)};
c.onFetchSuccess=function(M,O){Pl(A);K(M,O)}}try{y&&d.retry&&!d.ab.bypassNetworkless?(g.method="POST",d.ab.writeThenSend?Em().writeThenSend(q,g):Em().sendAndWrite(q,g)):R("web_all_payloads_via_jspb")?Hi(q,g):(g.method="POST",g.postParams||(g.postParams={}),Hi(q,g))}catch(M){if("InvalidAccessError"==M.name)A&&(Pl(A),A=0),ai(Error("An extension is blocking network request."));
else throw M;}A&&Wi(function(){Ql(a)},5E3)}
!P("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&ai(new aj("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new aj("innertube xhrclient not ready",b,c,d);$h(f);throw f;}var g={headers:d.headers||{},method:"POST",postParams:c,postBody:d.postBody,postBodyFormat:d.postBodyFormat||"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(y,A){if(d.onSuccess)d.onSuccess(A)},
onFetchSuccess:function(y){if(d.onSuccess)d.onSuccess(y)},
onError:function(y,A){if(d.onError)d.onError(A)},
onFetchError:function(y){if(d.onError)d.onError(y)},
timeout:d.timeout,withCredentials:!0};g.headers["Content-Type"]||(g.headers["Content-Type"]="application/json");var h="";(f=a.config_.xb)&&(h=f);var k=a.config_.zb||!1,l=Kl(k,h,d);Object.assign(g.headers,l);(f=g.headers.Authorization)&&!h&&(g.headers["x-origin"]=window.location.origin);var m="/youtubei/"+a.config_.vb+"/"+b,n={alt:"json"},r=a.config_.yb&&f;r=r&&f.startsWith("Bearer");r||(n.key=a.config_.ub);var q=ti(""+h+m,n||{},!0);C("ytNetworklessLoggingInitializationOptions")&&Hm.isNwlInitialized?
el().then(function(y){e(y)}):e(!1)}
;var Jm=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function Km(a){this.G=a;this.h=null;this.m=0;this.C=null;this.u=0;this.i=[];for(a=0;4>a;a++)this.i.push(0);this.l=0;this.Ga=ji(window,"mousemove",Va(this.Ha,this));this.Ia=li(Va(this.V,this),25)}
D(Km,pe);Km.prototype.Ha=function(a){void 0===a.h&&ei(a);var b=a.h;void 0===a.i&&ei(a);this.h=new Fd(b,a.i)};
Km.prototype.V=function(){if(this.h){var a=Jm();if(0!=this.m){var b=this.C,c=this.h,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.m);this.i[this.l]=.5<Math.abs((d-this.u)/this.u)?1:0;for(c=b=0;4>c;c++)b+=this.i[c]||0;3<=b&&this.G();this.u=d}this.m=a;this.C=this.h;this.l=(this.l+1)%4}};
Km.prototype.ba=function(){window.clearInterval(this.Ia);hi(this.Ga)};var Lm={};
function Mm(){var a={},b=void 0===a.Cb?!1:a.Cb;a=void 0===a.rb?!0:a.rb;if(null==C("_lact",window)){var c=parseInt(P("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;B("_lact",c,window);B("_fact",c,window);-1==c&&Nm();ji(document,"keydown",Nm);ji(document,"keyup",Nm);ji(document,"mousedown",Nm);ji(document,"mouseup",Nm);b?ji(window,"touchmove",function(){Om("touchmove",200)},{passive:!0}):(ji(window,"resize",function(){Om("resize",200)}),a&&ji(window,"scroll",function(){Om("scroll",200)}));
new Km(function(){Om("mouse",100)});
ji(document,"touchstart",Nm,{passive:!0});ji(document,"touchend",Nm,{passive:!0})}}
function Om(a,b){Lm[a]||(Lm[a]=!0,We.L(function(){Nm();Lm[a]=!1},b))}
function Nm(){null==C("_lact",window)&&Mm();var a=Date.now();B("_lact",a,window);-1==C("_fact",window)&&B("_fact",a,window);(a=C("ytglobal.ytUtilActivityCallback_"))&&a()}
function Pm(){var a=C("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;var Qm=z.ytPubsubPubsubInstance||new N,Rm=z.ytPubsubPubsubSubscribedKeys||{},Sm=z.ytPubsubPubsubTopicToKeys||{},Tm=z.ytPubsubPubsubIsSynchronous||{};N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.na;N.prototype.publish=N.prototype.ea;N.prototype.clear=N.prototype.clear;B("ytPubsubPubsubInstance",Qm);B("ytPubsubPubsubTopicToKeys",Sm);B("ytPubsubPubsubIsSynchronous",Tm);B("ytPubsubPubsubSubscribedKeys",Rm);var Um=Symbol("injectionDeps");function Vm(){this.i=new Map;this.h=new Map}
Vm.prototype.resolve=function(a){return Wm(this,a,[])};
function Wm(a,b,c){var d=void 0===d?!1:d;if(-1<c.indexOf(b))throw Error("Deps cycle for: "+b);if(a.h.has(b))return a.h.get(b);if(!a.i.has(b)){if(d)return;throw Error("No provider for: "+b);}d=a.i.get(b);c.push(b);if(d.Jb)var e=d.Jb;else if(d.Ib)e=d[Um]?Xm(a,d[Um],c):[],e=d.Ib.apply(d,ia(e));else if(d.Hb){e=d.Hb;var f=e[Um]?Xm(a,e[Um],c):[];e=new (Function.prototype.bind.apply(e,[null].concat(ia(f))))}else throw Error("Could not resolve providers for: "+b);c.pop();d.mc||a.h.set(b,e);return e}
function Xm(a,b,c){return b?b.map(function(d){return Wm(a,d,c)}):[]}
;var Ym;function Zm(){this.store={};this.h={}}
Zm.prototype.storePayload=function(a,b){a=$m(a);this.store[a]?this.store[a].push(b):(this.h={},this.store[a]=[b]);return a};
Zm.prototype.extractMatchingEntries=function(a){a=an(this,a);for(var b=[],c=0;c<a.length;c++)this.store[a[c]]&&(b.push.apply(b,ia(this.store[a[c]])),delete this.store[a[c]]);return b};
Zm.prototype.getSequenceCount=function(a){a=an(this,a);for(var b=0,c=0;c<a.length;c++)b+=this.store[a[c]].length||0;return b};
function an(a,b){var c=$m(b);if(a.h[c])return a.h[c];var d=Object.keys(a.store)||[];if(1>=d.length&&$m(b)===d[0])return d;for(var e=[],f=0;f<d.length;f++){var g=d[f].split("/");if(bn(b.auth,g[0])){var h=b.isJspb;bn(void 0===h?"undefined":h?"true":"false",g[1])&&bn(b.cttAuthInfo,g[2])&&e.push(d[f])}}return a.h[c]=e}
function bn(a,b){return void 0===a||"undefined"===a?!0:a===b}
Zm.prototype.getSequenceCount=Zm.prototype.getSequenceCount;Zm.prototype.extractMatchingEntries=Zm.prototype.extractMatchingEntries;Zm.prototype.storePayload=Zm.prototype.storePayload;function $m(a){return[void 0===a.auth?"undefined":a.auth,void 0===a.isJspb?"undefined":a.isJspb,void 0===a.cttAuthInfo?"undefined":a.cttAuthInfo].join("/")}
;var cn=wi("initial_gel_batch_timeout",2E3),dn=Math.pow(2,16)-1,en=void 0;function fn(){this.j=this.h=this.i=0}
var gn=new fn,hn=new fn,jn,kn=!0,ln=z.ytLoggingTransportGELQueue_||new Map;B("ytLoggingTransportGELQueue_",ln);var mn=z.ytLoggingTransportGELProtoQueue_||new Map;B("ytLoggingTransportGELProtoQueue_",mn);var nn=z.ytLoggingTransportTokensToCttTargetIds_||{};B("ytLoggingTransportTokensToCttTargetIds_",nn);var on=z.ytLoggingTransportTokensToJspbCttTargetIds_||{};B("ytLoggingTransportTokensToJspbCttTargetIds_",on);var pn={};function qn(){var a=C("yt.logging.ims");a||(a=new Zm,B("yt.logging.ims",a));return a}
function rn(a,b){R("web_all_payloads_via_jspb")&&ai(new aj("transport.log called for JSON in JSPB only experiment"));if("log_event"===a.endpoint){sn(a);var c=tn(a);if(R("use_new_in_memory_storage")){pn[c]=!0;var d={cttAuthInfo:c,isJspb:!1};qn().storePayload(d,a.payload);un(b,[],c,!1,d)}else d=ln.get(c)||[],ln.set(c,d),d.push(a.payload),un(b,d,c)}}
function vn(a,b){if("log_event"===a.endpoint){sn(void 0,a);var c=tn(a,!0);if(R("use_new_in_memory_storage")){pn[c]=!0;var d={cttAuthInfo:c,isJspb:!0};qn().storePayload(d,a.payload.toJSON());un(b,[],c,!0,d)}else d=mn.get(c)||[],mn.set(c,d),a=a.payload.toJSON(),d.push(a),un(b,d,c,!0)}}
function un(a,b,c,d,e){d=void 0===d?!1:d;a&&(en=new a);a=wi("tvhtml5_logging_max_batch")||wi("web_logging_max_batch")||100;var f=U(),g=d?hn.j:gn.j;b=b.length;e&&(b=qn().getSequenceCount(e));b>=a?jn||(jn=wn(function(){xn({writeThenSend:!0},R("flush_only_full_queue")?c:void 0,d);jn=void 0},0)):10<=f-g&&(yn(d),d?hn.j=f:gn.j=f)}
function zn(a,b){R("web_all_payloads_via_jspb")&&ai(new aj("transport.logIsolatedGelPayload called in JSPB only experiment"));if("log_event"===a.endpoint){sn(a);var c=tn(a),d=new Map;d.set(c,[a.payload]);b&&(en=new b);return new Xf(function(e,f){en&&en.isReady()?An(d,en,e,f,{bypassNetworkless:!0},!0):e()})}}
function Bn(a,b){if("log_event"===a.endpoint){sn(void 0,a);var c=tn(a,!0),d=new Map;d.set(c,[a.payload.toJSON()]);b&&(en=new b);return new Xf(function(e){en&&en.isReady()?Cn(d,en,e,{bypassNetworkless:!0},!0):e()})}}
function tn(a,b){var c="";if(a.ha)c="visitorOnlyApprovedKey";else if(a.cttAuthInfo){if(void 0===b?0:b){b=a.cttAuthInfo.token;c=a.cttAuthInfo;var d=new Mh;c.videoId?md(d,1,Nh,c.videoId):c.playlistId&&md(d,2,Nh,c.playlistId);on[b]=d}else b=a.cttAuthInfo,c={},b.videoId?c.videoId=b.videoId:b.playlistId&&(c.playlistId=b.playlistId),nn[a.cttAuthInfo.token]=c;c=a.cttAuthInfo.token}return c}
function xn(a,b,c){a=void 0===a?{}:a;c=void 0===c?!1:c;!c&&R("web_all_payloads_via_jspb")&&ai(new aj("transport.flushLogs called for JSON in JSPB only experiment"));new Xf(function(d,e){c?(Dn(hn.i),Dn(hn.h),hn.h=0):(Dn(gn.i),Dn(gn.h),gn.h=0);if(en&&en.isReady())if(R("use_new_in_memory_storage")){var f=a,g=c,h=en;f=void 0===f?{}:f;g=void 0===g?!1:g;var k=new Map,l=new Map;if(void 0!==b)g?(e=qn().extractMatchingEntries({isJspb:g,cttAuthInfo:b}),k.set(b,e),Cn(k,h,d,f)):(k=qn().extractMatchingEntries({isJspb:g,
cttAuthInfo:b}),l.set(b,k),An(l,h,d,e,f));else if(g){e=u(Object.keys(pn));for(g=e.next();!g.done;g=e.next())l=g.value,g=qn().extractMatchingEntries({isJspb:!0,cttAuthInfo:l}),0<g.length&&k.set(l,g),delete pn[l];Cn(k,h,d,f)}else{k=u(Object.keys(pn));for(g=k.next();!g.done;g=k.next()){g=g.value;var m=qn().extractMatchingEntries({isJspb:!1,cttAuthInfo:g});0<m.length&&l.set(g,m);delete pn[g]}An(l,h,d,e,f)}}else f=a,k=c,h=en,f=void 0===f?{}:f,k=void 0===k?!1:k,void 0!==b?k?(e=new Map,k=mn.get(b)||[],e.set(b,
k),Cn(e,h,d,f),mn.delete(b)):(k=new Map,l=ln.get(b)||[],k.set(b,l),An(k,h,d,e,f),ln.delete(b)):k?(Cn(mn,h,d,f),mn.clear()):(An(ln,h,d,e,f),ln.clear());else yn(c),d()})}
function yn(a){a=void 0===a?!1:a;if(R("web_gel_timeout_cap")&&(!a&&!gn.h||a&&!hn.h)){var b=wn(function(){xn({writeThenSend:!0},void 0,a)},6E4);
a?hn.h=b:gn.h=b}Dn(a?hn.i:gn.i);b=P("LOGGING_BATCH_TIMEOUT",wi("web_gel_debounce_ms",1E4));R("shorten_initial_gel_batch_timeout")&&kn&&(b=cn);b=wn(function(){xn({writeThenSend:!0},void 0,a)},b);
a?hn.i=b:gn.i=b}
function An(a,b,c,d,e,f){e=void 0===e?{}:e;var g=Math.round(U()),h=a.size,k={};a=u(a);for(var l=a.next();!l.done;k={pa:k.pa,U:k.U,fa:k.fa,ra:k.ra,qa:k.qa},l=a.next()){var m=u(l.value);l=m.next().value;m=m.next().value;k.U=mb({context:Cl(b.config_||Bl())});if(!Oa(m)&&!R("throw_err_when_logevent_malformed_killswitch")){d();break}k.U.events=m;(m=nn[l])&&En(k.U,l,m);delete nn[l];k.fa="visitorOnlyApprovedKey"===l;Fn(k.U,g,k.fa);Gn(e);k.ra=function(n){R("update_log_event_config")&&We.L(function(){return x(function(r){return w(r,
Hn(n),0)})});
h--;h||c()};
k.pa=0;k.qa=function(n){return function(){n.pa++;if(e.bypassNetworkless&&1===n.pa)try{Rl(b,"log_event",n.U,In({writeThenSend:!0},n.fa,n.ra,n.qa,f)),kn=!1}catch(r){$h(r),d()}h--;h||c()}}(k);
try{Rl(b,"log_event",k.U,In(e,k.fa,k.ra,k.qa,f)),kn=!1}catch(n){$h(n),d()}}}
function Cn(a,b,c,d,e){d=void 0===d?{}:d;var f=Math.round(U()),g=a.size,h=new Map([].concat(ia(a)));h=u(h);for(var k=h.next();!k.done;k=h.next()){var l=u(k.value).next().value,m=a.get(l);k=new Oh;var n=Jl(b.config_||Bl());J(k,sh,1,n);m=m?Jn(m):[];m=u(m);for(n=m.next();!n.done;n=m.next())td(k,3,Jh,n.value);(m=on[l])&&Kn(k,l,m);delete on[l];l="visitorOnlyApprovedKey"===l;Ln(k,f,l);Gn(d);k=Bd(k);l=In(d,l,function(r){R("update_log_event_config")&&We.L(function(){return x(function(q){return w(q,Hn(r),
0)})});
g--;g||c()},function(){g--;
g||c()},e);
l.headers["Content-Type"]="application/json+protobuf";l.postBodyFormat="JSPB";l.postBody=k;Rl(b,"log_event","",l);kn=!1}}
function Gn(a){R("always_send_and_write")&&(a.writeThenSend=!1)}
function In(a,b,c,d,e){a={retry:!0,onSuccess:c,onError:d,ab:a,ha:b,ec:!!e,headers:{},postBodyFormat:"",postBody:""};Mn()&&(a.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(U())));return a}
function Fn(a,b,c){Mn()||(a.requestTimeMs=String(b));R("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=P("EVENT_ID"))&&(c=Nn(),a.serializedClientEventId={serializedEventId:b,clientCounter:String(c)})}
function Ln(a,b,c){Mn()||I(a,2,b);if(!c&&(b=P("EVENT_ID"))){c=Nn();var d=new Lh;I(d,1,b);I(d,2,c);J(a,Lh,5,d)}}
function Nn(){var a=P("BATCH_CLIENT_COUNTER")||0;a||(a=Math.floor(Math.random()*dn/2));a++;a>dn&&(a=1);Uh("BATCH_CLIENT_COUNTER",a);return a}
function En(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function Kn(a,b,c){if(ud(c,1===nd(c,Nh)?1:-1))var d=1;else if(c.getPlaylistId())d=2;else return;J(a,Mh,4,c);a=od(a,sh,1)||new sh;c=od(a,qh,3)||new qh;var e=new ph;I(e,2,b);I(e,1,d);td(c,12,ph,e);J(a,qh,3,c)}
function Jn(a){for(var b=[],c=0;c<a.length;c++)try{b.push(new Jh(a[c]))}catch(d){$h(new aj("Transport failed to deserialize "+String(a[c])))}return b}
function sn(a,b){if(C("yt.logging.transport.enableScrapingForTest")){var c=C("yt.logging.transport.scrapedPayloadsForTesting"),d=C("yt.logging.transport.payloadToScrape","");b&&(b=C("yt.logging.transport.getScrapedPayloadFromClientEventsFunction").bind(b.payload)())&&c.push(b);a&&a.payload[d]&&c.push((null==a?void 0:a.payload)[d]);B("yt.logging.transport.scrapedPayloadsForTesting",c)}}
function Mn(){return R("use_request_time_ms_header")||R("lr_use_request_time_ms_header")}
function wn(a,b){return R("transport_use_scheduler")?Wi(a,b):ki(a,b)}
function Dn(a){R("transport_use_scheduler")?We.Z(a):window.clearTimeout(a)}
function Hn(a){var b,c,d,e,f,g,h,k,l,m;return x(function(n){if(1==n.h){d=null==(b=a)?void 0:null==(c=b.responseContext)?void 0:c.globalConfigGroup;var r=d?d[ch.name]:void 0;e=r;g=null==(f=d)?void 0:f.hotHashData;r=d?d[bh.name]:void 0;h=r;l=null==(k=d)?void 0:k.coldHashData;Ym||(Ym=new Vm);m=Ym.resolve(xl);return e&&g?w(n,yl(m,e,g),2):n.s(2)}return h&&l?w(n,zl(m,h,l),0):n.s(0)})}
;var On=z.ytLoggingGelSequenceIdObj_||{};B("ytLoggingGelSequenceIdObj_",On);
function Pn(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||U());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;R("enable_unknown_lact_fix_on_html5")&&Mm();a=Pm();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};R("log_sequence_info_on_gel_web")&&d.la&&(a=e.context,b=d.la,b={index:Qn(b),groupKey:b},a.sequence=b,d.sb&&delete On[d.la]);(d.Eb?zn:rn)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,ha:d.ha},c)}
function Rn(a){xn(void 0,void 0,void 0===a?!1:a)}
function Qn(a){On[a]=a in On?On[a]+1:0;return On[a]}
;var Sn=[];var Tn=z.ytLoggingGelSequenceIdObj_||{};B("ytLoggingGelSequenceIdObj_",Tn);function Un(a){var b=void 0;b=void 0===b?{}:b;var c=!1;P("ytLoggingEventsDefaultDisabled",!1)&&(c=!0);c=c?null:Im;b=void 0===b?{}:b;var d=Math.round(b.timestamp||U());I(a,1,d<Number.MAX_SAFE_INTEGER?d:0);var e=Pm();d=new Ih;I(d,1,b.timestamp||!isFinite(e)?-1:e);if(R("log_sequence_info_on_gel_web")&&b.la){e=b.la;var f=Qn(e),g=new Hh;I(g,2,f);I(g,1,e);J(d,Hh,3,g);b.sb&&delete Tn[b.la]}J(a,Ih,33,d);(b.Eb?Bn:vn)({endpoint:"log_event",payload:a,cttAuthInfo:b.cttAuthInfo,ha:b.ha},c)}
;function Vn(a,b){var c=void 0===c?{}:c;if(R("migrate_events_to_ts")){c=void 0===c?{}:c;c.timestamp=Math.round(c.timestamp||U());var d=Im;P("ytLoggingEventsDefaultDisabled",!1)&&Im===Im&&(d=null);R("web_all_payloads_via_jspb")?Sn.push({kc:a,payload:b,options:c}):Pn(a,b,d,c)}else d=Im,P("ytLoggingEventsDefaultDisabled",!1)&&Im==Im&&(d=null),Pn(a,b,d,c)}
;var Wn=[{La:function(a){return"Cannot read property '"+a.key+"'"},
Ba:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{La:function(a){return"Cannot call '"+a.key+"'"},
Ba:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{La:function(a){return a.key+" is not defined"},
Ba:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var Yn={T:[],R:[{nb:Xn,weight:500}]};function Xn(a){if("JavaException"===a.name)return!0;a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function Zn(){this.R=[];this.T=[]}
var $n;function ao(){if(!$n){var a=$n=new Zn;a.T.length=0;a.R.length=0;Yn.T&&a.T.push.apply(a.T,Yn.T);Yn.R&&a.R.push.apply(a.R,Yn.R)}return $n}
;var bo=new N;function co(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=eo(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=eo(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=eo(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function eo(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function fo(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=go(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=a[e];var g=b;var h=c;g="string"!==typeof f||"clickTrackingParams"!==e&&"trackingParams"!==e?0:(f=co(atob(f.replace(/-/g,"+").replace(/_/g,"/"))))?go(e+".ve",f,g,h):0;d+=g;d+=go(e,a[e],b,c);if(500<d)break}}else c[b]=ho(a),d+=c[b].length;else c[b]=ho(a),d+=c[b].length;return d}
function go(a,b,c,d){c+="."+a;a=ho(b);d[c]=a;return c.length+a.length}
function ho(a){try{return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}catch(b){return"unable to serialize "+typeof a+" ("+b.message+")"}}
;var io=new Set,jo=0,ko=0,lo=0,mo=[],no=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function oo(){for(var a=u(no),b=a.next();!b.done;b=a.next()){var c=Kb();if(c&&0<=c.toLowerCase().indexOf(b.value.toLowerCase()))return!0}return!1}
;function po(){var a;return x(function(b){return(a=qf())?b.return(a.then(function(c){c=Bd(c);for(var d=[],e=0,f=0;f<c.length;f++){var g=c.charCodeAt(f);255<g&&(d[e++]=g&255,g>>=8);d[e++]=g}return wc(d,3)})):b.return(Promise.resolve(null))})}
;var qo={};function ro(a){return qo[a]||(qo[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var so={},to=[],Kg=new N,uo={};function vo(){for(var a=u(to),b=a.next();!b.done;b=a.next())b=b.value,b()}
function wo(a,b){var c;"yt:"===a.tagName.toLowerCase().substr(0,3)?c=a.getAttribute(b):c=a?a.dataset?a.dataset[ro(b)]:a.getAttribute("data-"+b):null;return c}
function xo(a){Kg.ea.apply(Kg,arguments)}
;function yo(a){this.h=a||{};a=[this.h,window.YTConfig||{}];for(var b=0;b<a.length;b++)a[b].host&&(a[b].host=a[b].host.toString().replace("http://","https://"))}
function Z(a,b){a=[a.h,window.YTConfig||{}];for(var c=0;c<a.length;c++){var d=a[c][b];if(void 0!==d)return d}return null}
function zo(a,b,c){Ao||(Ao={},ji(window,"message",function(d){a:{if(d.origin===Z(a,"host")){try{var e=JSON.parse(d.data)}catch(f){e=void 0;break a}if(d=Ao[e.id])d.u=!0,d.u&&(E(d.m,d.sendMessage,d),d.m.length=0),d.Pa(e)}e=void 0}return e}));
Ao[c]=b}
var Ao=null;var Bo=window;
function Co(a,b,c){this.o=this.h=this.i=null;this.j=0;this.u=!1;this.m=[];this.l=null;this.G={};if(!a)throw Error("YouTube player element ID required.");this.id=Qa(this);this.C=c;c=document;if(a="string"===typeof a?c.getElementById(a):a)if(c="iframe"===a.tagName.toLowerCase(),b.host||(b.host=c?Rb(a.src):"https://www.youtube.com"),this.i=new yo(b),c||(b=Do(this,a),this.o=a,(c=a.parentNode)&&c.replaceChild(b,a),a=b),this.h=a,this.h.id||(this.h.id="widget"+Qa(this.h)),so[this.h.id]=this,window.postMessage){this.l=
new N;Eo(this);b=Z(this.i,"events");for(var d in b)b.hasOwnProperty(d)&&this.addEventListener(d,b[d]);for(var e in uo)uo.hasOwnProperty(e)&&Fo(this,e)}}
p=Co.prototype;p.setSize=function(a,b){this.h.width=a.toString();this.h.height=b.toString();return this};
p.getIframe=function(){return this.h};
p.Pa=function(a){Go(this,a.event,a)};
p.addEventListener=function(a,b){var c=b;"string"===typeof b&&(c=function(){window[b].apply(window,arguments)});
if(!c)return this;this.l.subscribe(a,c);Ho(this,a);return this};
function Fo(a,b){b=b.split(".");if(2===b.length){var c=b[1];a.C===b[0]&&Ho(a,c)}}
p.destroy=function(){this.h&&this.h.id&&(so[this.h.id]=null);var a=this.l;a&&"function"==typeof a.dispose&&a.dispose();if(this.o){a=this.h;var b=a.parentNode;b&&b.replaceChild(this.o,a)}else(a=this.h)&&a.parentNode&&a.parentNode.removeChild(a);Ao&&(Ao[this.id]=null);this.i=null;a=this.h;for(var c in kb)kb[c][0]==a&&hi(c);this.o=this.h=null};
p.Sa=function(){return{}};
function Io(a,b,c){c=c||[];c=Array.prototype.slice.call(c);b={event:"command",func:b,args:c};a.u?a.sendMessage(b):a.m.push(b)}
function Go(a,b,c){a.l.j||(c={target:a,data:c},a.l.ea(b,c),xo(a.C+"."+b,c))}
function Do(a,b){var c=document.createElement("iframe");b=b.attributes;for(var d=0,e=b.length;d<e;d++){var f=b[d].value;null!=f&&""!==f&&"null"!==f&&c.setAttribute(b[d].name,f)}c.setAttribute("frameBorder","0");c.setAttribute("allowfullscreen","1");c.setAttribute("allow","accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");c.setAttribute("title","YouTube "+Z(a.i,"title"));(b=Z(a.i,"width"))&&c.setAttribute("width",b.toString());(b=Z(a.i,"height"))&&c.setAttribute("height",
b.toString());var g=a.Sa();g.enablejsapi=window.postMessage?1:0;window.location.host&&(g.origin=window.location.protocol+"//"+window.location.host);g.widgetid=a.id;window.location.href&&E(["debugjs","debugcss"],function(k){var l=Zb(window.location.href,k);null!==l&&(g[k]=l)});
var h=""+Z(a.i,"host")+("/embed/"+Z(a.i,"videoId"))+"?"+Tb(g);Bo.yt_embedsEnableUaChProbe?po().then(function(k){var l=new URL(h),m=Number(l.searchParams.get("reloads"));isNaN(m)&&(m=0);l.searchParams.set("reloads",(m+1).toString());k&&l.searchParams.set("uach",k);l.searchParams.set("uats",Math.floor(window.performance.timeOrigin).toString());k=Td(l.href).toString();Pd(c,Wd(k));return k}):Bo.yt_embedsEnableIframeSrcWithIntent?Pd(c,Wd(h)):c.src=h;
return c}
p.bb=function(){this.h&&this.h.contentWindow?this.sendMessage({event:"listening"}):window.clearInterval(this.j)};
function Eo(a){zo(a.i,a,a.id);a.j=li(a.bb.bind(a),250);ji(a.h,"load",function(){window.clearInterval(a.j);a.j=li(a.bb.bind(a),250)})}
function Ho(a,b){a.G[b]||(a.G[b]=!0,Io(a,"addEventListener",[b]))}
p.sendMessage=function(a){a.id=this.id;a.channel="widget";var b=JSON.stringify(a),c=[Rb(this.h.src||"").replace("http:","https:")];if(this.h.contentWindow)for(var d=0;d<c.length;d++)try{this.h.contentWindow.postMessage(b,c[d])}catch(Ub){if(Ub.name&&"SyntaxError"===Ub.name){if(!(Ub.message&&0<Ub.message.indexOf("target origin ''"))){var e=void 0,f=Ub;e=void 0===e?{}:e;e.name=P("INNERTUBE_CONTEXT_CLIENT_NAME",1);e.version=P("INNERTUBE_CONTEXT_CLIENT_VERSION");var g=e||{},h="WARNING";h=void 0===h?"ERROR":
h;if(f){f.hasOwnProperty("level")&&f.level&&(h=f.level);if(R("console_log_js_exceptions")){var k=f,l=[];l.push("Name: "+k.name);l.push("Message: "+k.message);k.hasOwnProperty("params")&&l.push("Error Params: "+JSON.stringify(k.params));k.hasOwnProperty("args")&&l.push("Error args: "+JSON.stringify(k.args));l.push("File name: "+k.fileName);l.push("Stacktrace: "+k.stack);window.console.log(l.join("\n"),k)}if(!(5<=jo)){var m=void 0,n=void 0,r=f,q=g,y=Jd(r),A=y.message||"Unknown Error",H=y.name||"UnknownError",
K=y.stack||r.i||"Not available";if(K.startsWith(H+": "+A)){var M=K.split("\n");M.shift();K=M.join("\n")}var O=y.lineNumber||"Not available",pb=y.fileName||"Not available",uc=K,Aa=0;if(r.hasOwnProperty("args")&&r.args&&r.args.length)for(var ra=0;ra<r.args.length&&!(Aa=fo(r.args[ra],"params."+ra,q,Aa),500<=Aa);ra++);else if(r.hasOwnProperty("params")&&r.params){var X=r.params;if("object"===typeof r.params)for(n in X){if(X[n]){var ba="params."+n,ca=ho(X[n]);q[ba]=ca;Aa+=ba.length+ca.length;if(500<Aa)break}}else q.params=
ho(X)}if(mo.length)for(var W=0;W<mo.length&&!(Aa=fo(mo[W],"params.context."+W,q,Aa),500<=Aa);W++);navigator.vendor&&!q.hasOwnProperty("vendor")&&(q["device.vendor"]=navigator.vendor);var S={message:A,name:H,lineNumber:O,fileName:pb,stack:uc,params:q,sampleWeight:1},Zj=Number(r.columnNumber);isNaN(Zj)||(S.lineNumber=S.lineNumber+":"+Zj);if("IGNORED"===r.level)m=0;else a:{for(var ak=ao(),bk=u(ak.T),Yf=bk.next();!Yf.done;Yf=bk.next()){var ck=Yf.value;if(S.message&&S.message.match(ck.ic)){m=ck.weight;
break a}}for(var dk=u(ak.R),Zf=dk.next();!Zf.done;Zf=dk.next()){var ek=Zf.value;if(ek.nb(S)){m=ek.weight;break a}}m=1}S.sampleWeight=m;for(var fk=u(Wn),$f=fk.next();!$f.done;$f=fk.next()){var ag=$f.value;if(ag.Ba[S.name])for(var gk=u(ag.Ba[S.name]),bg=gk.next();!bg.done;bg=gk.next()){var hk=bg.value,Ud=S.message.match(hk.regexp);if(Ud){S.params["params.error.original"]=Ud[0];for(var cg=hk.groups,ik={},Vb=0;Vb<cg.length;Vb++)ik[cg[Vb]]=Ud[Vb+1],S.params["params.error."+cg[Vb]]=Ud[Vb+1];S.message=ag.La(ik);
break}}}S.params||(S.params={});var jk=ao();S.params["params.errorServiceSignature"]="msg="+jk.T.length+"&cb="+jk.R.length;S.params["params.serviceWorker"]="false";z.document&&z.document.querySelectorAll&&(S.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));sb("sample").constructor!==rb&&(S.params["params.fconst"]="true");var ua=S;window.yterr&&"function"===typeof window.yterr&&window.yterr(ua);if(0!==ua.sampleWeight&&!io.has(ua.message)){if("ERROR"===h){bo.ea("handleError",
ua);if(R("record_app_crashed_web")&&0===lo&&1===ua.sampleWeight)if(lo++,R("errors_via_jspb")){var dg=new Gh;I(dg,1,1);if(!R("report_client_error_with_app_crash_ks")){var kk=new Bh;I(kk,1,ua.message);var lk=new Ch;J(lk,Bh,3,kk);var mk=new Dh;J(mk,Ch,5,lk);var nk=new Eh;J(nk,Dh,9,mk);J(dg,Eh,4,nk)}var Oo=dg,ok=new Jh;rd(ok,Gh,20,Kh,Oo);Un(ok)}else{var pk={appCrashType:"APP_CRASH_TYPE_BREAKPAD"};R("report_client_error_with_app_crash_ks")||(pk.systemHealth={crashData:{clientError:{logMessage:{message:ua.message}}}});
Vn("appCrashed",pk)}ko++}else"WARNING"===h&&bo.ea("handleWarning",ua);if(R("kevlar_gel_error_routing"))a:{var eg=void 0,fg=void 0,Mc=h,Q=ua;if(R("errors_via_jspb")){if(oo())fg=void 0;else{var Wb=new yh;I(Wb,1,Q.stack);Q.fileName&&I(Wb,4,Q.fileName);var Ma=Q.lineNumber&&Q.lineNumber.split?Q.lineNumber.split(":"):[];0!==Ma.length&&(1!==Ma.length||isNaN(Number(Ma[0]))?2!==Ma.length||isNaN(Number(Ma[0]))||isNaN(Number(Ma[1]))||(I(Wb,2,Number(Ma[0])),I(Wb,3,Number(Ma[1]))):I(Wb,2,Number(Ma[0])));var vb=
new Bh;I(vb,1,Q.message);I(vb,3,Q.name);I(vb,6,Q.sampleWeight);"ERROR"===Mc?I(vb,2,2):"WARNING"===Mc?I(vb,2,1):I(vb,2,0);var gg=new zh;I(gg,1,!0);rd(gg,yh,3,Ah,Wb);var wb=new vh;I(wb,3,window.location.href);for(var qk=P("FEXP_EXPERIMENTS",[]),hg=0;hg<qk.length;hg++){var rk=wb,Po=qk[hg];Xc(rk);ld(rk,5,2,!1,!1).push(Po)}var ig=Vh();if(!Wh()&&ig)for(var sk=u(Object.keys(ig)),xb=sk.next();!xb.done;xb=sk.next()){var tk=xb.value,jg=new xh;I(jg,1,tk);I(jg,2,String(ig[tk]));td(wb,4,xh,jg)}var kg=Q.params;
if(kg){var uk=u(Object.keys(kg));for(xb=uk.next();!xb.done;xb=uk.next()){var vk=xb.value,lg=new xh;I(lg,1,"client."+vk);I(lg,2,String(kg[vk]));td(wb,4,xh,lg)}}var wk=P("SERVER_NAME"),xk=P("SERVER_VERSION");if(wk&&xk){var mg=new xh;I(mg,1,"server.name");I(mg,2,wk);td(wb,4,xh,mg);var ng=new xh;I(ng,1,"server.version");I(ng,2,xk);td(wb,4,xh,ng)}var Vd=new Ch;J(Vd,vh,1,wb);J(Vd,zh,2,gg);J(Vd,Bh,3,vb);fg=Vd}var yk=fg;if(!yk)break a;var zk=new Jh;rd(zk,Ch,163,Kh,yk);Un(zk)}else{if(oo())eg=void 0;else{var Nc=
{stackTrace:Q.stack};Q.fileName&&(Nc.filename=Q.fileName);var Na=Q.lineNumber&&Q.lineNumber.split?Q.lineNumber.split(":"):[];0!==Na.length&&(1!==Na.length||isNaN(Number(Na[0]))?2!==Na.length||isNaN(Number(Na[0]))||isNaN(Number(Na[1]))||(Nc.lineNumber=Number(Na[0]),Nc.columnNumber=Number(Na[1])):Nc.lineNumber=Number(Na[0]));var og={level:"ERROR_LEVEL_UNKNOWN",message:Q.message,errorClassName:Q.name,sampleWeight:Q.sampleWeight};"ERROR"===Mc?og.level="ERROR_LEVEL_ERROR":"WARNING"===Mc&&(og.level="ERROR_LEVEL_WARNNING");
var Qo={isObfuscated:!0,browserStackInfo:Nc},Xb={pageUrl:window.location.href,kvPairs:[]};P("FEXP_EXPERIMENTS")&&(Xb.experimentIds=P("FEXP_EXPERIMENTS"));var pg=Vh();if(!Wh()&&pg)for(var Ak=u(Object.keys(pg)),yb=Ak.next();!yb.done;yb=Ak.next()){var Bk=yb.value;Xb.kvPairs.push({key:Bk,value:String(pg[Bk])})}var qg=Q.params;if(qg){var Ck=u(Object.keys(qg));for(yb=Ck.next();!yb.done;yb=Ck.next()){var Dk=yb.value;Xb.kvPairs.push({key:"client."+Dk,value:String(qg[Dk])})}}var Ek=P("SERVER_NAME"),Fk=P("SERVER_VERSION");
Ek&&Fk&&(Xb.kvPairs.push({key:"server.name",value:Ek}),Xb.kvPairs.push({key:"server.version",value:Fk}));eg={errorMetadata:Xb,stackTrace:Qo,logMessage:og}}var Gk=eg;if(!Gk)break a;Vn("clientError",Gk)}if("ERROR"===Mc||R("errors_flush_gel_always_killswitch"))b:if(R("migrate_events_to_ts"))c:{if(R("web_fp_via_jspb")&&(Rn(!0),!R("web_fp_via_jspb_and_json")))break c;Rn()}else{if(R("web_fp_via_jspb")&&(Rn(!0),!R("web_fp_via_jspb_and_json")))break b;Rn()}}if(!R("suppress_error_204_logging")){var zb=ua,
Oc=zb.params||{},$a={urlParams:{a:"logerror",t:"jserror",type:zb.name,msg:zb.message.substr(0,250),line:zb.lineNumber,level:h,"client.name":Oc.name},postParams:{url:P("PAGE_NAME",window.location.href),file:zb.fileName},method:"POST"};Oc.version&&($a["client.version"]=Oc.version);if($a.postParams){zb.stack&&($a.postParams.stack=zb.stack);for(var Hk=u(Object.keys(Oc)),rg=Hk.next();!rg.done;rg=Hk.next()){var Ik=rg.value;$a.postParams["client."+Ik]=Oc[Ik]}var sg=Vh();if(sg)for(var Jk=u(Object.keys(sg)),
tg=Jk.next();!tg.done;tg=Jk.next()){var Kk=tg.value;$a.postParams[Kk]=sg[Kk]}var Lk=P("SERVER_NAME"),Mk=P("SERVER_VERSION");Lk&&Mk&&($a.postParams["server.name"]=Lk,$a.postParams["server.version"]=Mk)}Hi(P("ECATCHER_REPORT_HOST","")+"/error_204",$a)}try{io.add(ua.message)}catch(Vo){}jo++}}}}}else throw Ub;}else console&&console.warn&&console.warn("The YouTube player is not attached to the DOM. API calls should be made after the onReady event. See more: https://developers.google.com/youtube/iframe_api_reference#Events")};function Jo(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Ko(a){return 0===a.search("get")||0===a.search("is")}
;function Lo(a,b){Co.call(this,a,Object.assign({title:"video player",videoId:"",width:640,height:360},b||{}),"player");this.N={};this.playerInfo={};this.videoTitle=""}
v(Lo,Co);p=Lo.prototype;p.Sa=function(){var a=Z(this.i,"playerVars");if(a){var b={},c;for(c in a)b[c]=a[c];a=b}else a={};window!==window.top&&document.referrer&&(a.widget_referrer=document.referrer.substring(0,256));if(c=Z(this.i,"embedConfig")){if(Pa(c))try{c=JSON.stringify(c)}catch(d){console.error("Invalid embed config JSON",d)}a.embed_config=c}return a};
p.Pa=function(a){var b=a.event;a=a.info;switch(b){case "apiInfoDelivery":if(Pa(a))for(var c in a)a.hasOwnProperty(c)&&(this.N[c]=a[c]);break;case "infoDelivery":Mo(this,a);break;case "initialDelivery":Pa(a)&&(window.clearInterval(this.j),this.playerInfo={},this.N={},No(this,a.apiInterface),Mo(this,a));break;default:Go(this,b,a)}};
function Mo(a,b){if(Pa(b)){for(var c in b)b.hasOwnProperty(c)&&(a.playerInfo[c]=b[c]);a.playerInfo.hasOwnProperty("videoData")&&(b=a.playerInfo.videoData,b.hasOwnProperty("title")&&b.title?(b=b.title,b!==a.videoTitle&&(a.videoTitle=b,a.h.setAttribute("title",b))):(a.videoTitle="",a.h.setAttribute("title","YouTube "+Z(a.i,"title"))))}}
function No(a,b){E(b,function(c){this[c]||("getCurrentTime"===c?this[c]=function(){var d=this.playerInfo.currentTime;if(1===this.playerInfo.playerState){var e=(Date.now()/1E3-this.playerInfo.currentTimeLastUpdated_)*this.playerInfo.playbackRate;0<e&&(d+=Math.min(e,1))}return d}:Jo(c)?this[c]=function(){this.playerInfo={};
this.N={};Io(this,c,arguments);return this}:Ko(c)?this[c]=function(){var d=0;
0===c.search("get")?d=3:0===c.search("is")&&(d=2);return this.playerInfo[c.charAt(d).toLowerCase()+c.substr(d+1)]}:this[c]=function(){Io(this,c,arguments);
return this})},a)}
p.getVideoEmbedCode=function(){var a=Z(this.i,"host")+("/embed/"+Z(this.i,"videoId")),b=Number(Z(this.i,"width")),c=Number(Z(this.i,"height"));if(isNaN(b)||isNaN(c))throw Error("Invalid width or height property");b=Math.floor(b);c=Math.floor(c);var d=this.videoTitle;Gb.test(a)&&(-1!=a.indexOf("&")&&(a=a.replace(Ab,"&amp;")),-1!=a.indexOf("<")&&(a=a.replace(Bb,"&lt;")),-1!=a.indexOf(">")&&(a=a.replace(Cb,"&gt;")),-1!=a.indexOf('"')&&(a=a.replace(Db,"&quot;")),-1!=a.indexOf("'")&&(a=a.replace(Eb,"&#39;")),
-1!=a.indexOf("\x00")&&(a=a.replace(Fb,"&#0;")));return'<iframe width="'+b+'" height="'+c+'" src="'+a+'" title="'+((null!=d?d:"YouTube video player")+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')};
p.getOptions=function(a){return this.N.namespaces?a?this.N[a]?this.N[a].options||[]:[]:this.N.namespaces||[]:[]};
p.getOption=function(a,b){if(this.N.namespaces&&a&&b&&this.N[a])return this.N[a][b]};
function Ro(a){if("iframe"!==a.tagName.toLowerCase()){var b=wo(a,"videoid");b&&(b={videoId:b,width:wo(a,"width"),height:wo(a,"height")},new Lo(a,b))}}
;B("YT.PlayerState.UNSTARTED",-1);B("YT.PlayerState.ENDED",0);B("YT.PlayerState.PLAYING",1);B("YT.PlayerState.PAUSED",2);B("YT.PlayerState.BUFFERING",3);B("YT.PlayerState.CUED",5);B("YT.get",function(a){return so[a]});
B("YT.scan",vo);B("YT.subscribe",function(a,b,c){Kg.subscribe(a,b,c);uo[a]=!0;for(var d in so)so.hasOwnProperty(d)&&Fo(so[d],a)});
B("YT.unsubscribe",function(a,b,c){Jg(a,b,c)});
B("YT.Player",Lo);Co.prototype.destroy=Co.prototype.destroy;Co.prototype.setSize=Co.prototype.setSize;Co.prototype.getIframe=Co.prototype.getIframe;Co.prototype.addEventListener=Co.prototype.addEventListener;Lo.prototype.getVideoEmbedCode=Lo.prototype.getVideoEmbedCode;Lo.prototype.getOptions=Lo.prototype.getOptions;Lo.prototype.getOption=Lo.prototype.getOption;
to.push(function(a){var b=a;b||(b=document);a=gb(b.getElementsByTagName("yt:player"));var c=b||document;if(c.querySelectorAll&&c.querySelector)b=c.querySelectorAll(".yt-player");else{var d;c=document;b=b||c;if(b.querySelectorAll&&b.querySelector)b=b.querySelectorAll(".yt-player");else if(b.getElementsByClassName){var e=b.getElementsByClassName("yt-player");b=e}else{e=b.getElementsByTagName("*");var f={};for(c=d=0;b=e[c];c++){var g=b.className,h;if(h="function"==typeof g.split)h=0<=bb(g.split(/\s+/),
"yt-player");h&&(f[d++]=b)}f.length=d;b=f}}b=gb(b);E(fb(a,b),Ro)});
"undefined"!=typeof YTConfig&&YTConfig.parsetags&&"onload"!=YTConfig.parsetags||vo();var So=z.onYTReady;So&&So();var To=z.onYouTubeIframeAPIReady;To&&To();var Uo=z.onYouTubePlayerAPIReady;Uo&&Uo();}).call(this);
