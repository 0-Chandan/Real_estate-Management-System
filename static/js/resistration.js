let i=0;
function bl() {
    lc=document.getElementById("lc")
    lc.style.display="inline";
}
function lock() {
    lc=document.getElementById("lc")
    unlc=document.getElementById("unlc")
    pass=document.getElementById("pass")
    if(i==0)
    {
    pass.type=Text;
    unlc.style.display="inline";
    lc.style.display="none"
    i=1;
    }
else if(i==1)
    {
         pass.type="password";
        lc.style.display="inline"
        unlc.style.display="none";
         i=0;
        } 
}
