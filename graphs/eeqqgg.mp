% eeqqgg.mp -- do not edit, generated automatically by singelTop.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 10*28.45274pt#, 4*28.45274pt#, 0);
"feynmf: 1";
LaTeX_unitlength:=28.45274pt;
subgraph (0, 0, w, h);
vinit;
pickup pencircle scaled thin;
vleft (__e1, __e2);
vright (__l1, __l2);
vconnect ("fermion", __e1, __ipz);
vconnect ("fermion", __ipz, __e2);
vconnect ("dashes,label=$H$", __ipz, __opz);
vconnect ("fermion", __opz, __l1);
vconnect ("fermion", __l2, __opz);
vlabel ("$e^-$", __e1);
vlabel ("$e^+$", __e2);
vlabel ("$l^-$", __l1);
vlabel ("$l^+$", __l2);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
