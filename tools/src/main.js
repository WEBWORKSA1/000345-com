/* 000345 — site behaviour (no dependencies) */
(function(){
  "use strict";
  var d=document, root=d.documentElement;

  /* ---------- contact address: assembled only at click/submit time, never in markup ---------- */
  var K=__EM__;
  function addr(){var s="";for(var i=K.length-1;i>=0;i--){s+=String.fromCharCode(K[i]-7);}return s;}

  d.addEventListener("click",function(e){
    var a=e.target.closest&&e.target.closest("[data-mail]");
    if(!a)return;
    e.preventDefault();
    var subj=a.getAttribute("data-mail")||"Inquiry from 000345.com";
    window.location.href="mai"+"lto:"+addr()+"?subject="+encodeURIComponent(subj);
  });

  /* ---------- theme ---------- */
  try{var saved=localStorage.getItem("theme");if(saved)root.setAttribute("data-theme",saved);}catch(e){}
  var tb=d.querySelector(".theme-btn");
  if(tb){tb.addEventListener("click",function(){
    var cur=root.getAttribute("data-theme");
    if(!cur){cur=window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";}
    var next=cur==="dark"?"light":"dark";root.setAttribute("data-theme",next);
    try{localStorage.setItem("theme",next);}catch(e){}
  });}

  /* ---------- mobile menu ---------- */
  var mb=d.querySelector(".menu-btn"),nav=d.querySelector(".nav");
  if(mb&&nav){mb.addEventListener("click",function(){var o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o?"true":"false");});}

  /* ---------- cookie notice ---------- */
  var ck=d.querySelector(".cookie");
  var choice=null;try{choice=localStorage.getItem("cookie-choice");}catch(e){}
  if(ck&&!choice){ck.classList.add("show");}
  d.querySelectorAll("[data-cookie]").forEach(function(b){b.addEventListener("click",function(){
    var v=b.getAttribute("data-cookie");try{localStorage.setItem("cookie-choice",v);}catch(e){}
    if(v==="essential"){(window.adsbygoogle=window.adsbygoogle||[]).requestNonPersonalizedAds=1;}
    ck.classList.remove("show");
  });});
  if(choice==="essential"){(window.adsbygoogle=window.adsbygoogle||[]).requestNonPersonalizedAds=1;}

  /* ---------- year ---------- */
  d.querySelectorAll("[data-year]").forEach(function(n){n.textContent=new Date().getFullYear();});

  /* ---------- multi-step forms ---------- */
  d.querySelectorAll("form[data-steps]").forEach(function(f){
    var steps=f.querySelectorAll(".step"),bar=f.querySelectorAll(".steps-bar span"),i=0;
    function show(n){steps.forEach(function(s,k){s.classList.toggle("active",k===n);});bar.forEach(function(b,k){b.classList.toggle("on",k<=n);});i=n;
      var first=steps[n].querySelector("input,select,textarea");if(first&&n>0)first.focus();}
    function valid(n){var ok=true;steps[n].querySelectorAll("[required]").forEach(function(el){
      if(el.type==="radio"){if(!steps[n].querySelector('input[name="'+el.name+'"]:checked'))ok=false;}
      else if(!el.checkValidity()){ok=false;}});
      if(!ok){var msg=f.querySelector(".form-msg");msg.textContent="Fill in the highlighted fields to continue.";msg.className="form-msg show err";
        var bad=steps[n].querySelector(":invalid");if(bad)bad.reportValidity();}
      else{f.querySelector(".form-msg").className="form-msg";}
      return ok;}
    f.querySelectorAll("[data-next]").forEach(function(b){b.addEventListener("click",function(){if(valid(i))show(i+1);});});
    f.querySelectorAll("[data-prev]").forEach(function(b){b.addEventListener("click",function(){show(i-1);});});
    show(0);
  });

  /* ---------- form submission (relay service; address injected at send time) ---------- */
  d.querySelectorAll("form[data-form]").forEach(function(f){
    f.addEventListener("submit",function(e){
      e.preventDefault();
      var msg=f.querySelector(".form-msg"),btn=f.querySelector('[type="submit"]');
      if(f.querySelector('input[name="_honey"]').value){return;}
      if(!f.checkValidity()){f.reportValidity();return;}
      var data={};new FormData(f).forEach(function(v,k){if(k==="_honey")return;data[k]=data[k]?data[k]+", "+v:v;});
      data._subject="[000345.com] "+f.getAttribute("data-form");
      data._template="table";data._captcha="false";data.page=location.href;
      btn.disabled=true;var label=btn.textContent;btn.textContent="Sending…";
      fetch("https://formsubmit.co/ajax/"+addr(),{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
      .then(function(r){return r.json().catch(function(){return {};}).then(function(j){if(!r.ok)throw new Error("status");return j;});})
      .then(function(){
        msg.textContent=f.getAttribute("data-success")||"Received. We'll reply within one business day.";
        msg.className="form-msg show ok";f.reset();
        var steps=f.querySelectorAll(".step");if(steps.length){steps.forEach(function(s,k){s.classList.toggle("active",k===0);});f.querySelectorAll(".steps-bar span").forEach(function(b,k){b.classList.toggle("on",k===0);});}
        try{if(window.gtag)gtag("event","generate_lead",{form:f.getAttribute("data-form")});}catch(x){}
      })
      .catch(function(){
        msg.innerHTML='That didn’t send. Check your connection and try again, or <a href="#" data-mail="'+(f.getAttribute("data-form")||"Inquiry")+'">email us directly</a>.';
        msg.className="form-msg show err";
      })
      .finally(function(){btn.disabled=false;btn.textContent=label;});
    });
  });

  /* ---------- prefill quote form from ?project= and ?zip= ---------- */
  var qp=new URLSearchParams(location.search).get("project");
  if(qp){var r=d.querySelector('input[name="project_type"][value="'+qp.replace(/[^a-z]/g,"")+'"]');if(r)r.checked=true;}
  var qz=new URLSearchParams(location.search).get("zip"),zi=d.getElementById("q-zip");
  if(qz&&zi){zi.value=qz.slice(0,10);}

  /* ---------- privacy-friendly YouTube embeds (load on click) ---------- */
  d.querySelectorAll(".video .frame button[data-yt]").forEach(function(b){
    var id=b.getAttribute("data-yt");
    b.style.backgroundImage="url(https://i.ytimg.com/vi/"+id+"/hqdefault.jpg)";
    b.addEventListener("click",function(){
      var f=d.createElement("iframe");
      f.src="https://www.youtube-nocookie.com/embed/"+id+"?autoplay=1&rel=0";
      f.title=b.getAttribute("aria-label")||"Video";
      f.allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen=true;b.replaceWith(f);
    });
  });

  /* ---------- donation amount picker ---------- */
  d.querySelectorAll("[data-amount]").forEach(function(b){b.addEventListener("click",function(){
    var inp=d.getElementById("pledge-amount");if(inp){inp.value=b.getAttribute("data-amount");inp.focus();}
    d.querySelectorAll("[data-amount]").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false");});
  });});

  /* ---------- share buttons ---------- */
  d.querySelectorAll("[data-share]").forEach(function(b){b.addEventListener("click",function(){
    var u=location.href,t=d.title;
    if(navigator.share){navigator.share({title:t,url:u}).catch(function(){});}
    else{navigator.clipboard&&navigator.clipboard.writeText(u);b.textContent="Link copied";}
  });});
})();
