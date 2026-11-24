const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/carousel.html');for(let i=1;i<=8;i++){await (await p.$('#s'+i)).screenshot({path:`${__dirname}/slide-0${i}.png`});}await b.close();})();
