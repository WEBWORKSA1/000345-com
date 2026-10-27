/* 000345 calculator engine. Each .calc-box[data-calc] maps to a function below.
   All functions receive (v, sys) where v holds numeric input values and sys is "imp" or "met". */
(function(){
  "use strict";
  var d=document;
  function f(n,dec){if(!isFinite(n))return "—";dec=dec==null?2:dec;return Number(n).toLocaleString(undefined,{maximumFractionDigits:dec,minimumFractionDigits:0});}
  function ceil(n){return Math.ceil(n-1e-9);}
  function deg(r){return r*180/Math.PI;}
  function ftin(ft){ /* decimal feet -> 12' 3-1/4" (nearest 1/16") */
    if(!isFinite(ft))return "—";var neg=ft<0;ft=Math.abs(ft);
    var inch=Math.round(ft*12*16)/16,F=Math.floor(inch/12),I=inch-F*12,w=Math.floor(I),fr=Math.round((I-w)*16),num=fr,den=16;
    while(num&&num%2===0&&den>1){num/=2;den/=2;}
    var ins=(w||!num?String(w):"")+(num?(w?"-":"")+num+"/"+den:"")+'"';
    return (neg?"-":"")+F+"' "+ins;}
  function inch(i){return ftin(i/12).replace(/^-?0' /,function(m){return m.charAt(0)==="-"?"-":"";});}
  function len(x,sys){return sys==="imp"?ftin(x)+"  ("+f(x,3)+" ft)":f(x,3)+" m";}
  function R(label,val){return [label,val];}

  var C={};

  C.squaring=function(v,s){
    var a=v.a,b=v.b,out=[],notes=[];
    var c=Math.sqrt(a*a+b*b);
    out.push(R("Diagonal for a true 90°",len(c,s)));
    var k=Math.min(a/3,b/4);var unit=s==="imp"?1:0.5;var kk=Math.max(1,Math.floor(k/unit))*unit;
    if(k>=unit){out.push(R("Largest 3-4-5 that fits",f(3*kk)+" / "+f(4*kk)+" / "+f(5*kk)+(s==="imp"?" ft":" m")));}
    else{out.push(R("Suggested triangle",s==="imp"?"3 / 4 / 5 ft":"0.6 / 0.8 / 1.0 m"));}
    if(v.m>0){
      var cos=(a*a+b*b-v.m*v.m)/(2*a*b);cos=Math.max(-1,Math.min(1,cos));
      var ang=deg(Math.acos(cos)),dev=ang-90,off=b*Math.tan(Math.abs(dev)*Math.PI/180);
      out.push(R("Measured corner angle",f(ang,2)+"°"));
      out.push(R("Out of square by",s==="imp"?inch(off*12)+" at the end of side B":f(off*1000,0)+" mm at the end of side B"));
      notes.push(Math.abs(dev)<0.05?"<span class='ok'>Corner is square within 0.05°. Good to build.</span>":
        "<span class='warn'>"+(v.m>c?"Diagonal is long: the corner is open (wider than 90°). Swing side B inward.":"Diagonal is short: the corner is closed (tighter than 90°). Swing side B outward.")+"</span>");
    }
    return {out:out,notes:notes};
  };

  C.triangle=function(v,s){
    var a=v.a,b=v.b,c=v.c,n=[a,b,c].filter(function(x){return x>0;}).length;
    if(n<2)return {out:[],notes:["Enter any two sides. Leave the unknown side at 0."]};
    if(a>0&&b>0&&!(c>0))c=Math.sqrt(a*a+b*b);
    else if(a>0&&c>0&&!(b>0)){if(c<=a)return {out:[],notes:["<span class='warn'>Hypotenuse c must be longer than side a.</span>"]};b=Math.sqrt(c*c-a*a);}
    else if(b>0&&c>0&&!(a>0)){if(c<=b)return {out:[],notes:["<span class='warn'>Hypotenuse c must be longer than side b.</span>"]};a=Math.sqrt(c*c-b*b);}
    var u=s==="imp"?" ft":" m",au=s==="imp"?" ft²":" m²";
    var out=[R("Side a",f(a,4)+u),R("Side b",f(b,4)+u),R("Hypotenuse c",f(c,4)+u),
      R("Angle A",f(deg(Math.atan2(a,b)),3)+"°"),R("Angle B",f(deg(Math.atan2(b,a)),3)+"°"),
      R("Area",f(a*b/2,3)+au),R("Perimeter",f(a+b+c,3)+u)];
    var notes=[];if(n===3&&Math.abs(a*a+b*b-c*c)>1e-6*c*c)notes.push("<span class='warn'>These three sides do not form a right triangle (a² + b² ≠ c²).</span>");
    return {out:out,notes:notes};
  };

  C.rectangle=function(v,s){
    var ideal=Math.sqrt(v.l*v.l+v.w*v.w),out=[R("Ideal diagonal",len(ideal,s))],notes=[];
    if(v.d1>0&&v.d2>0){
      var diff=Math.abs(v.d1-v.d2),diffSmall=s==="imp"?diff*12:diff*1000;
      out.push(R("Diagonal difference",s==="imp"?inch(diffSmall):f(diffSmall,0)+" mm"));
      out.push(R("Approx. corner error",f(deg(Math.atan((diff/2)/ideal))*2,3)+"°"));
      var tol=s==="imp"?(v.l<10?0.125:0.25):(v.l<3?3:6);
      notes.push(diffSmall<=tol?"<span class='ok'>Within typical layout tolerance. Square.</span>":
        "<span class='warn'>Diagonals differ by more than typical tolerance ("+(s==="imp"?inch(tol):tol+" mm")+"). Rack the frame toward the shorter diagonal by half the difference.</span>");
    }
    return {out:out,notes:notes};
  };

  C.concrete=function(v,s){
    var w=1+v.waste/100,out=[],vol;
    if(s==="imp"){vol=v.l*v.w*(v.t/12)*w;var yd=vol/27;
      out=[R("Volume",f(yd,2)+" yd³"),R("Volume (metric)",f(yd*0.764555,2)+" m³"),R("80 lb bags",ceil(vol/0.6)),R("60 lb bags",ceil(vol/0.45)),R("Ready-mix order",f(Math.ceil(yd*4)/4,2)+" yd³")];}
    else{vol=v.l*v.w*(v.t/100)*w;
      out=[R("Volume",f(vol,2)+" m³"),R("Volume (imperial)",f(vol/0.764555,2)+" yd³"),R("25 kg bags",ceil(vol/0.012)),R("40 kg bags",ceil(vol/0.019)),R("Ready-mix order",f(Math.ceil(vol*4)/4,2)+" m³")];}
    return {out:out,notes:["Includes "+v.waste+"% for spillage, uneven subgrade and form bulge. Bag yields are typical manufacturer figures; check the bag you buy."]};
  };

  C.footing=function(v,s){
    var vol,out;
    if(s==="imp"){var r=v.dia/24;vol=Math.PI*r*r*(v.depth/12)*v.n*(1+v.waste/100);
      out=[R("Total volume",f(vol,2)+" ft³"),R("Cubic yards",f(vol/27,3)+" yd³"),R("80 lb bags",ceil(vol/0.6)),R("Per hole",f(vol/v.n,2)+" ft³")];}
    else{var rm=v.dia/200;vol=Math.PI*rm*rm*(v.depth/100)*v.n*(1+v.waste/100);
      out=[R("Total volume",f(vol,3)+" m³"),R("25 kg bags",ceil(vol/0.012)),R("Per hole",f(vol/v.n*1000,1)+" L")];}
    return {out:out,notes:[]};
  };

  C.pitch=function(v,s){
    var p=v.rise/v.run*12,ang=deg(Math.atan(v.rise/v.run)),fac=Math.sqrt(1+Math.pow(v.rise/v.run,2));
    var out=[R("Roof pitch",f(p,2)+" : 12"),R("Angle",f(ang,2)+"°"),R("Slope (grade)",f(v.rise/v.run*100,1)+"%"),R("Rafter multiplier",f(fac,4))];
    if(v.area>0)out.push(R("Sloped roof area",f(v.area*fac,0)+(s==="imp"?" ft²  ("+f(v.area*fac/100,1)+" squares)":" m²")));
    var notes=[];if(p<2)notes.push("<span class='warn'>Below 2:12 most shingle makers do not warrant asphalt shingles; plan for a low-slope membrane.</span>");
    else if(p<4)notes.push("2:12 to 4:12 is low slope: shingles usually need a double underlayment.");
    return {out:out,notes:notes};
  };

  C.rafter=function(v,s){
    var run=v.span/2,fac=Math.sqrt(1+Math.pow(v.pitch/12,2)),oh=s==="imp"?v.oh/12:v.oh/100;
    var L=run*fac+oh*fac,rise=run*v.pitch/12;
    return {out:[R("Rafter length (incl. overhang)",len(L,s)),R("Length to ridge (no overhang)",len(run*fac,s)),R("Ridge rise above wall",len(rise,s)),R("Plumb cut angle",f(deg(Math.atan(v.pitch/12)),2)+"°"),R("Board to buy",s==="imp"?(Math.ceil(L/2)*2)+" ft stock":f(Math.ceil(L*10/6)*0.6,1)+" m stock")],
      notes:["Measured along the top edge. Deduct half the ridge-board thickness at the peak."]};
  };

  C.stairs=function(v,s){
    var n=Math.max(1,Math.ceil(v.rise/v.target)),r=v.rise/n,t=n-1,run=t*v.tread,str=Math.sqrt(v.rise*v.rise+run*run);
    var out=[R("Number of risers",n),R("Riser height",s==="imp"?inch(r):f(r,1)+" cm"),R("Number of treads",t),R("Total run",s==="imp"?inch(run):f(run,1)+" cm"),R("Stringer length",s==="imp"?inch(str):f(str,1)+" cm"),R("Stair angle",f(deg(Math.atan(v.rise/run)),1)+"°")];
    var notes=[],maxR=s==="imp"?7.75:19.6,minT=s==="imp"?10:25.4;
    notes.push(r<=maxR?"<span class='ok'>Riser is within the common residential maximum ("+(s==="imp"?"7¾\"":"196 mm")+").</span>":"<span class='warn'>Riser exceeds the common residential maximum. Add a riser.</span>");
    notes.push(v.tread>=minT?"<span class='ok'>Tread depth meets the common residential minimum.</span>":"<span class='warn'>Tread is shallower than the common residential minimum.</span>");
    var rule=2*r+v.tread;
    notes.push(s==="imp"?"Comfort check (2 × riser + tread): "+f(rule,1)+"\" — 24\" to 25\" feels natural.":"Comfort check (2 × riser + tread): "+f(rule,1)+" cm — 61 to 64 cm feels natural.");
    return {out:out,notes:notes};
  };

  C.deck=function(v,s){
    var bw=s==="imp"?(v.bw+v.gap)/12:(v.bw+v.gap)/1000,rows=ceil(v.w/bw),per=ceil(v.l/v.bl),boards=ceil(rows*per*(1+v.waste/100));
    var sp=s==="imp"?16/12:0.4,joists=Math.floor(v.l/sp)+1;
    return {out:[R("Board rows",rows),R("Boards to buy",boards+" × "+f(v.bl)+(s==="imp"?" ft":" m")),R("Linear "+(s==="imp"?"feet":"metres"),f(boards*v.bl,0)),R("Deck area",f(v.l*v.w,1)+(s==="imp"?" ft²":" m²")),R("Joists (16\" / 400 mm o.c.)",joists),R("Screws (2 per crossing)",f(rows*joists*2*1.05,0))],
      notes:["Boards run along the length. Butt joints should land on a joist — stagger them so no two adjacent rows break on the same joist."]};
  };

  C.tile=function(v,s){
    var area=v.l*v.w,ta=s==="imp"?((v.tl+v.g)*(v.tw+v.g))/144:((v.tl+v.g/10)*(v.tw+v.g/10))/10000;
    var tiles=ceil(area/ta*(1+v.waste/100));
    return {out:[R("Floor/wall area",f(area,2)+(s==="imp"?" ft²":" m²")),R("Tiles needed",tiles),R("Boxes",v.box>0?ceil(tiles/v.box):"—"),R("Tiles per "+(s==="imp"?"ft²":"m²"),f(1/ta,2))],
      notes:["Use 10% waste for straight lay, 15% for diagonal or herringbone, and keep a few spares from the same dye lot."]};
  };

  C.paint=function(v,s){
    var walls=2*(v.l+v.w)*v.h,door=s==="imp"?21:1.9,win=s==="imp"?15:1.4;
    var area=walls-v.doors*door-v.windows*win+(v.ceil===1?v.l*v.w:0);area=Math.max(0,area);
    var need=area*v.coats/v.cov;
    return {out:[R("Paintable area",f(area,0)+(s==="imp"?" ft²":" m²")),R("Paint needed",f(need,2)+(s==="imp"?" gal":" L")),R("Buy",s==="imp"?(Math.floor(need)+" gal + "+ceil((need-Math.floor(need))*4)+" qt"):ceil(need)+" L"),R("Primer (1 coat)",f(area/v.cov,2)+(s==="imp"?" gal":" L"))],
      notes:["Door ≈ "+(s==="imp"?"21 ft²":"1.9 m²")+", window ≈ "+(s==="imp"?"15 ft²":"1.4 m²")+". Rough or porous surfaces can cut coverage by 20–30%."]};
  };

  C.drywall=function(v,s){
    var area=2*(v.l+v.w)*v.h+(v.ceil===1?v.l*v.w:0)-v.open;area=Math.max(0,area);
    var sheetA=s==="imp"?(v.sheet===2?48:32):(v.sheet===2?3.6:2.88),sheets=ceil(area/sheetA*1.1);
    var sqft=s==="imp"?area:area*10.7639;
    return {out:[R("Wall + ceiling area",f(area,0)+(s==="imp"?" ft²":" m²")),R("Sheets (incl. 10%)",sheets),R("Joint tape",f(sqft*0.37,0)+" ft"),R("Ready-mix compound",f(sqft*0.138,0)+" lb (~"+ceil(sqft*0.138/61.7)+" × 4.5 gal pails)"),R("Screws",f(sheets*32,0))],
      notes:["Tape and compound use the long-standing ratio of about 370 ft tape and 138 lb ready-mix per 1,000 ft² of board."]};
  };

  C.flooring=function(v,s){
    var area=v.l*v.w,tot=area*(1+v.waste/100);
    return {out:[R("Room area",f(area,2)+(s==="imp"?" ft²":" m²")),R("Area with waste",f(tot,2)+(s==="imp"?" ft²":" m²")),R("Boxes",v.box>0?ceil(tot/v.box):"—"),R("Underlayment",f(area*1.05,0)+(s==="imp"?" ft²":" m²"))],
      notes:["Acclimate wood and laminate in the room for 48–72 hours before installing."]};
  };

  C.gravel=function(v,s){
    var dens={1:[1.4,1.66],2:[0.4,0.47],3:[1.1,1.3],4:[1.35,1.6]}[v.mat]||[1.4,1.66];
    var out;
    if(s==="imp"){var ft3=v.l*v.w*(v.depth/12),yd=ft3/27;
      out=[R("Volume",f(yd,2)+" yd³"),R("Weight",f(yd*dens[0],2)+" US tons"),R("2 ft³ bags",ceil(ft3/2)),R("Volume (metric)",f(yd*0.764555,2)+" m³")];}
    else{var m3=v.l*v.w*(v.depth/100);
      out=[R("Volume",f(m3,2)+" m³"),R("Weight",f(m3*dens[1],2)+" tonnes"),R("50 L bags",ceil(m3*1000/50)),R("Volume (imperial)",f(m3/0.764555,2)+" yd³")];}
    return {out:out,notes:["Weights are typical dry densities. Wet or crushed material can be 10–20% heavier — confirm with your supplier."]};
  };

  C.fence=function(v,s){
    var sections=ceil(v.len/v.sp),posts=sections+1+v.gates,rails=sections*v.rails;
    var pw=s==="imp"?(v.pw+v.pg)/12:(v.pw+v.pg)/1000,pickets=ceil(v.len/pw*1.05);
    return {out:[R("Posts",posts),R("Sections",sections),R("Rails",rails),R("Pickets (+5%)",pickets),R("Concrete bags (2 per post)",posts*2)],
      notes:["Set corner and end posts first, string a line between them, and square any corner with the 3-4-5 rule before setting line posts."]};
  };

  C.area=function(v,s){
    var a=v.l1*v.w1+v.l2*v.w2+v.l3*v.w3+v.tb*v.th/2,u=s==="imp"?" ft²":" m²";
    var out=[R("Total area",f(a,2)+u),R(s==="imp"?"Square metres":"Square feet",f(s==="imp"?a/10.7639:a*10.7639,2)+(s==="imp"?" m²":" ft²"))];
    if(v.price>0)out.push(R("Estimated cost",f(a*v.price,2)));
    return {out:out,notes:["Break L-shaped or irregular rooms into rectangles plus one triangle, measure each, and add them."]};
  };

  C.boardfeet=function(v,s){
    var bf,out;
    if(s==="imp"){bf=v.t*v.w*v.l/12*v.q;out=[R("Board feet",f(bf,2)),R("Cubic feet",f(bf/12,3)),R("Cost",v.price>0?f(bf*v.price,2):"—")];}
    else{var m3=(v.t/1000)*(v.w/1000)*v.l*v.q;bf=m3*423.776;out=[R("Cubic metres",f(m3,4)),R("Board feet",f(bf,2)),R("Cost",v.price>0?f(m3*v.price,2):"—")];}
    return {out:out,notes:["Hardwood is sold by nominal rough thickness: 4/4 = 1\", 8/4 = 2\". Use the nominal figure."]};
  };

  C.brick=function(v,s){
    var area=Math.max(0,v.l*v.h-v.open),per=s==="imp"?144/((v.bl+v.j)*(v.bh+v.j)):10000/((v.bl/10+v.j/10)*(v.bh/10+v.j/10));
    var bricks=ceil(area*per*(1+v.waste/100));
    return {out:[R("Wall area",f(area,1)+(s==="imp"?" ft²":" m²")),R("Bricks per "+(s==="imp"?"ft²":"m²"),f(per,2)),R("Bricks needed",bricks),R("Mortar (rule of thumb)",ceil(bricks/1000*7)+" bags masonry cement")],
      notes:["Mortar uses the common rule of about 7 bags of masonry cement per 1,000 modular bricks with a 3/8\" (10 mm) joint."]};
  };

  /* ---------- wiring ---------- */
  function boxSys(box){try{return localStorage.getItem("units")||box.getAttribute("data-default-sys")||"imp";}catch(e){return "imp";}}
  function setSys(box,sys){
    box.setAttribute("data-sys",sys);
    box.querySelectorAll(".unit-switch button").forEach(function(b){b.setAttribute("aria-pressed",b.getAttribute("data-sys")===sys?"true":"false");});
    box.querySelectorAll("[data-imp]").forEach(function(inp){
      var unit=inp.getAttribute("data-u-"+sys),lab=box.querySelector('label[for="'+inp.id+'"] .u');
      if(lab)lab.textContent=unit?" ("+unit+")":"";
      var def=inp.getAttribute("data-"+sys);if(inp.tagName==="INPUT"&&def!=null)inp.value=def;
    });
    run(box);
  }
  function run(box){
    var fn=C[box.getAttribute("data-calc")],sys=box.getAttribute("data-sys")||"imp",v={};
    box.querySelectorAll("input,select").forEach(function(i){if(i.name)v[i.name]=parseFloat(i.value)||0;});
    var res,html="";
    try{res=fn(v,sys);}catch(e){res={out:[],notes:["Check your inputs."]};}
    if(res.out.length){html+="<dl>";res.out.forEach(function(p){html+='<div class="r"><dt>'+p[0]+"</dt><dd>"+p[1]+"</dd></div>";});html+="</dl>";}
    res.notes.forEach(function(n){html+='<p class="note">'+n.replace("class='ok'","style='color:var(--ok);font-weight:600'")+"</p>";});
    box.querySelector(".results").innerHTML=html;
  }
  d.querySelectorAll(".calc-box[data-calc]").forEach(function(box){
    box.querySelectorAll(".unit-switch button").forEach(function(b){b.addEventListener("click",function(){var s=b.getAttribute("data-sys");try{localStorage.setItem("units",s);}catch(e){}setSys(box,s);});});
    box.addEventListener("input",function(){run(box);});
    box.addEventListener("change",function(){run(box);});
    var r=box.querySelector("[data-reset]");if(r)r.addEventListener("click",function(){setSys(box,box.getAttribute("data-sys"));});
    var p=box.querySelector("[data-print]");if(p)p.addEventListener("click",function(){window.print();});
    setSys(box,boxSys(box));
  });

  /* ---------- hero squaring visual ---------- */
  var sq=d.getElementById("squarer");
  if(sq){
    var A=sq.querySelector("#sq-a"),B=sq.querySelector("#sq-b"),M=sq.querySelector("#sq-m"),svg=sq.querySelector("svg"),out=sq.querySelector(".verdict");
    function draw(){
      var a=parseFloat(A.value)||0,b=parseFloat(B.value)||0,m=parseFloat(M.value)||0;if(a<=0||b<=0)return;
      var c=Math.sqrt(a*a+b*b),ang=90;
      if(m>0){var cs=(a*a+b*b-m*m)/(2*a*b);cs=Math.max(-1,Math.min(1,cs));ang=deg(Math.acos(cs));}
      var W=420,H=300,pad=46,sc=Math.min((W-2*pad)/b,(H-2*pad)/a)*0.92,ox=pad,oy=H-pad;
      var rad=ang*Math.PI/180,bx=ox+b*sc,by=oy,ax=ox+a*sc*Math.cos(rad),ay=oy-a*sc*Math.sin(rad);
      ax=ox+(ax-ox);var ok=Math.abs(ang-90)<0.05;
      var col=ok?"var(--ok)":"var(--marker)";
      svg.innerHTML='<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="var(--line)" stroke-width=".6"/></pattern></defs>'+
        '<rect width="'+W+'" height="'+H+'" fill="url(#g)"/>'+
        '<line x1="'+ox+'" y1="'+oy+'" x2="'+bx+'" y2="'+by+'" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>'+
        '<line x1="'+ox+'" y1="'+oy+'" x2="'+ax+'" y2="'+ay+'" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>'+
        '<line x1="'+ax+'" y1="'+ay+'" x2="'+bx+'" y2="'+by+'" stroke="var(--chalk)" stroke-width="3" stroke-dasharray="8 6"/>'+
        (ok?'<path d="M'+(ox+18)+' '+oy+'V'+(oy-18)+'H'+ox+'" fill="none" stroke="var(--ok)" stroke-width="2.5"/>':'<circle cx="'+ox+'" cy="'+oy+'" r="16" fill="none" stroke="var(--marker)" stroke-width="2.5"/>')+
        '<text x="'+((ox+bx)/2)+'" y="'+(oy+28)+'" text-anchor="middle" font-family="Barlow Condensed,Arial Narrow,sans-serif" font-size="22" font-weight="700" fill="var(--ink)">B = '+f(b)+'</text>'+
        '<text x="'+(ox-12)+'" y="'+((oy+ay)/2)+'" text-anchor="end" font-family="Barlow Condensed,Arial Narrow,sans-serif" font-size="22" font-weight="700" fill="var(--ink)" transform="rotate(-90 '+(ox-12)+' '+((oy+ay)/2)+')">A = '+f(a)+'</text>'+
        '<text x="'+((ax+bx)/2+10)+'" y="'+((ay+by)/2-8)+'" font-family="Barlow Condensed,Arial Narrow,sans-serif" font-size="22" font-weight="700" fill="var(--chalk)">'+(m>0?"measured "+f(m):"target "+f(c,3))+'</text>'+
        '<text x="'+(ox+24)+'" y="'+(oy-24)+'" font-family="Source Sans 3,sans-serif" font-size="15" font-weight="700" fill="'+col+'">'+f(ang,2)+'°</text>';
      if(m>0){var dev=ang-90;out.className="verdict "+(ok?"ok":"off");
        out.textContent=ok?"Square. Your diagonal matches the target of "+f(c,3)+".":(dev>0?"Open by ":"Closed by ")+f(Math.abs(dev),2)+"°. The diagonal should read "+f(c,3)+" — you measured "+f(m,3)+".";}
      else{out.className="verdict";out.textContent="Measure "+f(a)+" along one side, "+f(b)+" along the other. Move the corner until the diagonal reads exactly "+f(c,3)+".";}
    }
    [A,B,M].forEach(function(i){i.addEventListener("input",draw);});draw();
  }
})();
