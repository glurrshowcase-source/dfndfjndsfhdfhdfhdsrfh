from pathlib import Path
import json, sys
p=Path(sys.argv[1])
f=p/"src/modules/gxlx/loading.cpp"
s=f.read_text(encoding="utf-8")
def sub(a,b,v):
 global s
 i=s.index(a); j=s.index(b,i)
 s=s[:i]+v+s[j:]
s=s.replace("        CCSprite* barFire = nullptr;\n        CCSprite* barHead = nullptr;\n        CCSprite* barOutline = nullptr;", "        CCProgressTimer* barFill = nullptr;")
sub("        // Two copies of the supplied bar:", "        f->percent =", """        // Empty red frame, with separately clipped fire underneath.
        f->barTrack = makeSprite("loading-bar-frame.png", 5);
        auto firePath = utils::string::pathToString(gxlx::resource("loading-bar-fire.png"));
        if (auto* fire = CCSprite::create(firePath.c_str())) {
            f->barFill = CCProgressTimer::create(fire);
            if (f->barFill) {
                f->barFill->setType(kCCProgressTimerTypeBar);
                f->barFill->setMidpoint({0.f, 0.5f});
                f->barFill->setBarChangeRate({1.f, 0.f});
                f->barFill->setPercentage(0.f);
                f->cover->addChild(f->barFill, 6);
            }
        }

""")
sub("        // Image geometry is measured", "        if (f->percent) {", """        constexpr float frameWidth = 1948.f;
        constexpr float frameHeight = 236.f;
        const float scale = size.width * 0.72f / frameWidth;
        const float centerX = size.width * 0.5f;
        const float centerY = size.height * 0.19f;
        constexpr float fireCenterOffset = ((138.f + 1908.f) * 0.5f) - 1024.f;
        if (f->barTrack) {
            f->barTrack->setScale(scale);
            f->barTrack->setPosition({centerX, centerY});
        }
        if (f->barFill) {
            f->barFill->setScale(scale);
            f->barFill->setPosition({centerX + fireCenterOffset * scale, centerY});
            f->barFill->setPercentage(std::clamp(f->progress * 100.f, 0.f, 100.f));
        }
""")
s=s.replace("centerY - 118.f * scale - 8.f","centerY - frameHeight * 0.5f * scale - 10.f")
assert "CCProgressTimer" in s and "setTextureRect" not in s and "barOutline" not in s
f.write_text(s,encoding="utf-8")
m=p/"mod.json"; meta=json.loads(m.read_text(encoding="utf-8")); assert meta["version"]=="v1.1.7"
meta["version"]="v1.1.8"; meta["description"]="GxLx 1.1.8 - fixed fiery loading bar"
m.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
c=p/"CMakeLists.txt"; t=c.read_text(encoding="utf-8")
assert "project(GxLx VERSION 1.1.7" in t
c.write_text(t.replace("project(GxLx VERSION 1.1.7","project(GxLx VERSION 1.1.8"),encoding="utf-8")
unused=p/"resources/GxLx/loading-bar-outline.png"
if unused.exists(): unused.unlink()
print("GxLx 1.1.8 loading bar fixed")
