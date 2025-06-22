float h(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}
vec3 m(float t){
    t=clamp(t,0.,1.);
    return t<.25?mix(vec3(.02,.05,.2),vec3(.1,.2,.5),t/.25):t<.5?mix(vec3(.1,.2,.5),vec3(0.,.2,.8),(t-.25)/.25):t<.85?mix(vec3(0.,.2,.8),vec3(.3,.7,1.),(t-.5)/.35):t<.97?mix(vec3(.3,.7,1.),vec3(.7,.9,1.),(t-.85)/.12):vec3(.7,.9,1.);
}
void mainImage(out vec4 o,in vec2 f){
    vec2 r=iResolution.xy,u=(floor(f/6.)*6.+3.)/r,c=(u-.5)*2.;
    c.x*=r.x/r.y;
    float d=length(c);
    if(d>.92){o=vec4(0);return;}
    vec2 w=c;
    w.x+=.4*sin(w.y*2.+iTime*1.2);
    w.y+=.4*cos(w.x*2.-iTime);
    w+=.15*vec2(sin(w.y*5.+iTime*.8),cos(w.x*5.-iTime*.8));
    w+=.05*vec2(h(floor(w*30.)),h(floor(w*30.+10.)));
    vec2 q=u-vec2(.65);
    float s=length(q),a=atan(q.y,q.x)+5.*s;
    w*=mix(.85,1.,smoothstep(0.,.35,s));
    float v=mix(sin(8.*w.x+10.*w.y+iTime*1.5),sin(5.*a+iTime*1.2+2.*sin(5.*s-iTime*2.)),smoothstep(.5,0.,s));
    o=vec4(m(v*.5+.5)*smoothstep(.92,.7,d),1.);
}
