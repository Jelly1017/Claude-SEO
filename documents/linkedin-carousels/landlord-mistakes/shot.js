const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/graphic.html');
await (await p.$('#p')).screenshot({path:__dirname+'/landlord-mistakes-portrait.png'});
await (await p.$('#q')).screenshot({path:__dirname+'/landlord-mistakes-square.png'});await b.close();})();
