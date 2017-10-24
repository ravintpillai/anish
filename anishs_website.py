from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
	return render_template('contact.html')


@app.route('/anish_related_things')
def anish_related_things():
	return "This program made on GitHub, is related to the guy sometimes known as Anish Mariathasan."

@app.route('/about')
def other_thing():
	return "This fabulous website was made by a person, who got the domain as a gift from an epic guy..."

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact. Sadly. But, if you know how to navigate the internet, you can find me..."

if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
	

<!doctype html>
<html lang="en">
<head>
    <script type="text/javascript">
                (function () {
                    var appName = 'wix-homepage-davinci';
                    window.fedops = window.fedops || {};
                    window.fedops.apps = window.fedops.apps || {};
                    window.fedops.apps[appName] = { startLoadTime: window.performance && window.performance.now && window.performance.now() };
                    window.fedops.sessionId = window.localStorage.getItem('fedops.logger.sessionId') || 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) { var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8); return v.toString(16); });
                    (new Image()).src = '//frog.wix.com/fed?appName=' + appName + '&src=72&evid=14&session_id=' + window.fedops.sessionId;
                })();
    </script>
    <script type="text/javascript">
    window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(15),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,o){try{d?d-=1:i("err",[o||new UncaughtException(t,e,n)])}catch(s){try{i("ierr",[s,(new Date).getTime(),!0])}catch(c){}}return"function"==typeof f&&f.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t){i("err",[t,(new Date).getTime()])}var i=t("handle"),a=t(16),s=t("ee"),c=t("loader"),f=window.onerror,u=!1,d=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(l){"stack"in l&&(t(8),t(7),"addEventListener"in window&&t(5),c.xhrWrappable&&t(9),u=!0)}s.on("fn-start",function(t,e,n){u&&(d+=1)}),s.on("fn-err",function(t,e,n){u&&(this.thrown=!0,o(n))}),s.on("fn-end",function(){u&&!this.thrown&&d>0&&(d-=1)}),s.on("internal-error",function(t){i("ierr",[t,(new Date).getTime(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(8),s=t(7),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",y="pushState";t("loader").features.stn=!0,t(6);var g=NREUM.o.EV;o.on(m,function(t,e){var n=t[0];n instanceof g&&(this.bstStart=Date.now())}),o.on(w,function(t,e){var n=t[0];n instanceof g&&i("bst",[n,e,this.bstStart,Date.now()])}),a.on(m,function(t,e,n){this.bstStart=Date.now(),this.bstType=n}),a.on(w,function(t,e){i(v,[e,this.bstStart,Date.now(),this.bstType])}),s.on(m,function(){this.bstStart=Date.now()}),s.on(w,function(t,e){i(v,[e,this.bstStart,Date.now(),"requestAnimationFrame"])}),o.on(y+p,function(t){this.time=Date.now(),this.startPath=location.pathname+location.hash}),o.on(y+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,!1),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),s=t(17)(a),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){if(t[1]){var n=t[1];if("function"==typeof n){var r=c(n,"nr@wrapped",function(){return s(n,"fn-",null,n.name||"anonymous")});this.wrapped=t[1]=r}else"function"==typeof n.handleEvent&&s.inPlace(n,["handleEvent"],"fn-")}}),a.on(d+"-start",function(t){var e=this.wrapped;e&&(t[1]=e)})},{}],6:[function(t,e,n){var r=t("ee").get("history"),o=t(17)(r);e.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],7:[function(t,e,n){var r=t("ee").get("raf"),o=t(17)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],8:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration="number"==typeof t[1]?t[1]:0,t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(17)(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],9:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,w,"fn-",s)}function i(t){v.push(t),h&&(g=-g,b.data=g)}function a(){for(var t=0;t<v.length;t++)r([],v[t]);v.length&&(v=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(5);var f=t("ee"),u=f.get("xhr"),d=t(17)(u),l=NREUM.o,p=l.XHR,h=l.MO,m="readystatechange",w=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],v=[];e.exports=u;var y=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(m,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(p,y),y.prototype=p.prototype,d.inPlace(y.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var g=1,b=document.createTextNode(g);new h(a).observe(b,{characterData:!0})}else f.on("fn-end",function(t){t[0]&&t[0].type===m||a()})},{}],10:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=(new Date).getTime()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var a=t.getResponseHeader("X-NewRelic-App-Data");a&&(e.cat=a.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),s("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return h(r)}function i(t,e){var n=c(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var s=t("handle"),c=t(11),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(14),h=t(13),m=window.XMLHttpRequest;a.features.xhr=!0,t(9),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=h(r);i&&(n.txSize=i)}this.startTime=(new Date).getTime(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var a=0;a<d;a++)e.addEventListener(u[a],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=(new Date).getTime()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[(new Date).getTime()-this.xhrCbStart,this.onload,e],e)})}},{}],11:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],12:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[(new Date).getTime()].concat(s(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(15),s=t(16),c=t("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var u=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],d="api-",l=d+"ixn-";a(u,function(t,e){f[e]=o(d+e,!0,"api")}),f.addPageAction=o(d+"addPageAction",!0),e.exports=newrelic,f.interaction=function(){return(new r).get()};var p=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(l+"tracer",[Date.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return e.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){p[e]=o(l+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,(new Date).getTime()])}},{}],13:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],14:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],15:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],16:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],17:[function(t,e,n){function r(t){return!(t&&"function"==typeof t&&t.apply&&!t[a])}var o=t("ee"),i=t(16),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;e.exports=function(t){function e(t,e,n,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof n?n(r,a):n||{}}catch(u){d([u,"",[r,a,o],s])}f(e+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(l){throw f(e+"err",[r,a,l],s),l}finally{f(e+"end",[r,a,c],s)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,u(t,nrWrapper),nrWrapper)}function n(t,n,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<n.length;c++)s=n[c],a=t[s],r(a)||(t[s]=e(a,f?s+o:o,i,s))}function f(e,n,r){if(!c){c=!0;try{t.emit(e,n,r)}catch(o){d([o,e,n,r])}c=!1}}function u(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){d([r])}for(var o in t)s.call(t,o)&&(e[o]=t[o]);return e}function d(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),e.inPlace=n,e.flag=a,e}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?s(t,a,i):i()}function n(n,r,o){t&&t(n,r,o);for(var i=e(o),a=l(n),s=a.length,c=0;c<s;c++)a[c].apply(i,r);var u=f[w[n]];return u&&u.push([v,n,r,i]),i}function d(t,e){m[t]=l(t).concat(e)}function l(t){return m[t]||[]}function p(t){return u[t]=u[t]||o(n)}function h(t,e){c(t,function(t,n){e=e||"feature",w[n]=e,e in f||(f[e]=[])})}var m={},w={},v={on:d,emit:n,get:p,listeners:l,context:e,buffer:h};return v}function i(){return new r}var a="nr@context",s=t("gos"),c=t(15),f={},u={},d=e.exports=o();d.backlog=f},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!g++){var t=y.info=NREUM.info,e=u.getElementsByTagName("script")[0];if(t&&t.licenseKey&&t.applicationID&&e){c(w,function(e,n){t[e]||(t[e]=n)});var n="https"===m.split(":")[0]||t.sslForHttp;y.proto=n?"https://":"//",s("mark",["onload",a()],null,"api");var r=u.createElement("script");r.src=y.proto+t.agent,e.parentNode.insertBefore(r,e)}}}function o(){"complete"===u.readyState&&i()}function i(){s("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var s=t("handle"),c=t(15),f=window,u=f.document,d="addEventListener",l="attachEvent",p=f.XMLHttpRequest,h=p&&p.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:p,REQ:f.Request,EV:f.Event,PR:f.Promise,MO:f.MutationObserver},t(12);var m=""+location,w={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-974.min.js"},v=p&&h&&h[d]&&!/CriOS/.test(navigator.userAgent),y=e.exports={offset:a(),origin:m,features:{},xhrWrappable:v};u[d]?(u[d]("DOMContentLoaded",i,!1),f[d]("load",r,!1)):(u[l]("onreadystatechange",o),f[l]("onload",r)),s("mark",["firstbyte",a()],null,"api");var g=0},{}]},{},["loader",2,10,4,3]);
    ;NREUM.info={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",licenseKey:"c99d7f1ab0",applicationID:"32997699",sa:1}
    </script>
    <script>
        window.loadTime = Date.now();
        window.__LOCALE__ = "en";
        window.scrollTo(0, 0);

        function getLocationOrigin() {
            var origin = window.location.origin;
            if (!window.location.origin) {
                origin = "https://" + window.location.hostname + (window.location.port ? ":" + window.location.port : "");
            }
            return origin;
        };

        function reportBI(extension, src, evid, report) {
          var base = "https://frog.wix.com/";

          report = report || [];
          report.push("evid=" + evid);

          if (typeof(src) !== "string") {
            report.push("src=" + src);
          }

          if (extension === "hp") {
            report.push("version=adi homepage");
            report.push("origin=" + getLocationOrigin());
          }

          report.push("_=" + new Date().getTime());

          var img = new Image();
          img.src = base + extension + "?" + report.join("&");
        }

        reportBI('hp', '19', '315');



<!--[if lt IE 9]>
  <script src="https://static.parastorage.com/services/wix-homepage-davinci/1.337.0/bower_components/wix-header-and-footer/dist/bower_components/html5shiv/dist/html5shiv.js"></script>
<![endif]-->

<link rel="stylesheet" type="text/css" href="https://static.parastorage.com/services/wix-homepage-davinci/1.337.0/bower_components/wix-header-and-footer/dist/styles/header.css">

<!--add class "transparent" for the  transparent version-->
<nav id="wix-menu" class="wix-menu initializing" lang="en">
  <a href="https://www.wix.com" id="wm-logo">Wix</a>
  <ul class="web">
    <li class="is-hidden davinci-hide" id="wm-verticals-link"><a id="wm-site-for" href="https://www.wix.com/new/vertical?referralAdditionalInfo=header">I Need a Site for...</a></li>
    <li class="is-hidden davinci-hide" id="wm-verticals-drop-down"></li>
    <li class="is-hidden davinci-hide" id="wm-verticals-names">
      {"BUSINESS":"Business","MUSIC":"Music","PHOTOGRAPHY":"Photography","ONLINE_STORE":"Online Store","DESIGNER":"Designer","RESTAURANTS":"Restaurants & Food","ACCOMMODATION":"Accommodation","EVENTS":"Events","PORTFOLIO_AND_CV":"Portfolio & CV","BEAUTY_AND_WELLNESS":"Beauty & Wellness","BLOG":"Blog","OTHER":"Other"}
    </li>
    <li><a id="wm-my-account-link" href="https://www.wix.com/my-account">My Sites</a></li>
    <li class="davinci-hide"><a class="wm-create-link" href="https://www.wix.com/website/templates">Templates</a></li>
    <li class="davinci-hide">
      <a class="wm-explore-link" href="https://www.wix.com/explore/websites">
        Explore
        <span class="sub-menu-arrow"><svg width="10" height="5.7" viewBox="0 0 10 5.7"><polygon fill="none" points="5 5.7 0 0.7 0.7 0 5 4.4 9.3 0 10 0.7 "/></svg></span>
      </a>
      <ul class="wm-submenu">
        <li>
          <a id="wm-get-inspired-link" href="https://www.wix.com/explore/websites">
            <span>Get Inspired</span>
          </a>
        </li>
        <li>
          <a class="wm-features-link" href="https://www.wix.com/features/main">
            <span>Features</span>
          </a>
        </li>
        <li>
          <a id="wm-app-market-link" href="https://www.wix.com/app-market/main">
            <span>App Market</span>
          </a>
        </li>
      </ul>
    </li>
    <li class="davinci-show"><a class="wm-features-link" href="https://www.wix.com/features/main"><span>Features</span></a></li>
    <li class="davinci-show"><a class="wm-explore-link" href="https://www.wix.com/explore/websites">Explore</a></li>
    <li>
      <a id="wm-subscriptions" href="https://www.wix.com/upgrade/website">
        Subscriptions
        <span class="sub-menu-arrow"><svg width="10" height="5.7" viewBox="0 0 10 5.7"><polygon fill="none" points="5 5.7 0 0.7 0.7 0 5 4.4 9.3 0 10 0.7 "/></svg></span>
      </a>
      <ul class="wm-submenu">
        <li>
          <a id="wm-sub-upgrade-plans" href="https://www.wix.com/upgrade/website">
            <span>Premium Plans</span>
          </a>
        </li>
        <li>
          <a id="wm-sub-domains" href="https://www.wix.com/domain/names">
            <span>Domains</span>
          </a>
        </li>
        <li>
          <a id="wm-sub-mail-box" href="https://www.wix.com/about/mailboxes">
            <span>Mailboxes</span>
          </a>
        </li>
      </ul>
    </li>
    <li class="davinci-show"><a class="wm-create-link" href="https://www.wix.com/website/templates">Templates</a></li>
    <li><a id="wm-support-link" href="https://support.wix.com/en/">Support</a></li>
  </ul>
  <div id="wm-user-component">
    <a target="_self" href="https://www.wix.com/signin?loginDialogContext=login&referralInfo=HEADER" class="wm-signin">Sign In</a>
    <div class="wm-logged-in">
      <div id="wm-user-greeting">
        Hi, {username}
        <span class="sub-menu-arrow"><svg width="10" height="5.7" viewBox="0 0 10 5.7"><polygon fill="none" points="5 5.7 0 0.7 0.7 0 5 4.4 9.3 0 10 0.7 "/></svg></span>
      </div>
      <ul id="wm-settings-drop-down">
        <li><a target="_self" href="https://www.wix.com/my-account/settings">Account Settings</a></li>
        <li><a target="_self" href="https://premium.wix.com/wix/api/PaymentConsole">Billing & Payments</a></li>
        <li><a target="_self" href="https://premium.wix.com/wix/api/voucherConsole">Vouchers</a></li>
        <li id="wm-settings-language-dropdown"></li>
        <li><a target="_self" href="https://www.wix.com/signout">Logout</a></li>
      </ul>
    </div>
  </div>
  <div id="wm-mobile-sidebar">
    <ul class="wm-mobile-menu-links">
      <li id="wm-mobile-get-started"><a href class="get-started" bi="origin=header">Get Started</a></li>
      <li><a href="https://www.wix.com" id="wm-homepage-link" bi="wix">Home</a></li>
      <li><a href="https://www.wix.com/features/main" id="wm-features-link" bi="features/main">Features</a></li>
      <li><a href="https://www.wix.com/domain/names" id="wm-domains-link" bi="domain/names">Domains</a></li>
      <li><a href="https://www.wix.com/about/mailboxes" id="wm-mailboxes-link" bi="about/mailboxes">Mailboxes</a></li>
      <li><a href="https://www.wix.com/ecommerce/website" id="wm-ecommerce-link" bi="ecommerce/website">Online Store</a></li>
      <li><a href="https://www.wix.com/about/contact-us" id="wm-contact-us" bi="about/contact-us">Contact Us</a></li>
      <li><a href="https://www.wix.com/jobs/home" id="wm-jobs" bi="jobs/home" avoidHttps="true">Jobs</a></li>


      <li><a avoidHttps="true" href="https://www.wix.com/blog" id="wm-mobile-blog" bi="blog">Wix Blog</a></li>

      <li><a avoidHttps="true" href="https://www.wix.com/stories/" id="wm-stories" bi="stories">Wix Stories</a></li>
    </ul>
  </div>

</nav>

<script type="text/javascript">

var W = W || {};
W.Site = W.Site || {};
W.Site.Common = W.Site.Common || {};
W.Site.Common.clientTopology = W.Site.Common.clientTopology || {};
W.Site.Common.clientTopology.premiumBaseUrl =  'https://premium.wix.com';
W.Site.Common.clientTopology.usersBaseUrl = 'https://users.wix.com';
W.Site.Common.clientTopology.baseUrl = 'https://www.wix.com';
W.Site.Common.clientTopology.headerAndFooterStaticsUrl = 'https://static.parastorage.com/services/wix-homepage-davinci/1.337.0/bower_components/wix-header-and-footer/dist/';

</script>
<script type="text/javascript" src="https://static.parastorage.com/services/wix-homepage-davinci/1.337.0/bower_components/wix-header-and-footer/dist/scripts/scripts.js"></script>

</header>
<main>
    <section class="home-wrapper">
        <div class=" fold home" data-fold="1" id="home-fold">

            <div class="video-wrapper" id="video-wrapper">
                <video
                   id="video-player"
                   loop
                    muted>
                    <source src="https://video.wixstatic.com/video/ed0ad3_3b60553ecb2548338bb27b7b95213c39/1080p/mp4/file.mp4"  type="video/mp4"/>
                    <track src="https://static.parastorage.com/services/wix-homepage-davinci/1.337.0/caption/subtitles_en.vtt" kind="captions" srclang="en" label="en"/>
                    <p>A man looks out towards the city skyline.</p>
                </video>
                <div id="video-player-placeholder" class="video-player-bg"></div>
            </div>
            <div class="forground">
                <div class="inner">
                    <h1 >It All Sta<span class='text-fix'>rt</span>s with Your Stunning Website</h1>
                    <p class="text" >Wix unites beauty and advanced technology to create your stunning website. It’s easy and free.</p>
                    <button class="cta" fold-name="1" id="mainCta">Start Now</button>
                </div>
            </div>
        </div>
    </section>

    <section class="content">
        <div class="row fold" data-fold="2">
            <div class="vw50 text-wrapper left">
                <div class="feature">
                    <hr class="divider"/>
                    <h2 class="fix-space-ie" id="content-first-title">Everything You Need to</br>Create Your Stunning Website</h2>
                    <p class="text">
                        We’ve got you covered. Free websites, easy drag and </br>drop, designer-made templates, beautiful galleries,</br>mobile optimized, domains, huge image collection, </br>secure hosting, SEO, 24/7 full support and more -</br>all wrapped up in one free website builder.
