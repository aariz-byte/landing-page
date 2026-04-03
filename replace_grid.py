import sys

with open('index.html', 'r') as f:
    content = f.read()

start_marker = '<div class="bg">'
end_marker = '      <div class="cta-r rv" style="margin-top:6rem">'

parts = content.split(start_marker)
if len(parts) < 2:
    print("Start marker not found")
    sys.exit(1)

pre_content = parts[0]
rest = parts[1]

end_parts = rest.split(end_marker)
if len(end_parts) < 2:
    print("End marker not found")
    sys.exit(1)

post_content = end_parts[1]

new_grid = """
        <div class="bc sp2 rvs">
          <div class="bc-img" style="background: linear-gradient(135deg, #2a2a2a, #1a1a1a);">[ Search UI Screenshot ]</div>
          <div class="bc-grid-icon">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div class="bc-content">
            <div class="bc-head">
              <div class="bc-lb">Semantic Search</div>
              <div class="bc-tt" style="font-size: clamp(2rem, 3.5vw, 2.5rem); letter-spacing:-0.03em;">Search by feeling,<br>not keywords</div>
            </div>
          </div>
          <div class="bc-cta-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg></div>
        </div>
        
        <div class="bc feat rvs" style="justify-content: center;">
          <div class="bc-img"
            style="background-image:radial-gradient(rgba(255,255,255,0.15) 2px, transparent 2px);background-size:24px 24px;background-position:center bottom;background-repeat:repeat;height:60%;top:auto;bottom:0">
          </div>
          <div class="bc-content">
            <div class="bc-head">
              <div style="display: flex; justify-content: space-between; font-size: 0.75rem; letter-spacing: 0.05em; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 0.5rem; margin-bottom: 2rem;">
                <span>Product Lineup</span>
                <span>8/8</span>
              </div>
              <div class="bc-tt" style="font-size: clamp(2rem, 3vw, 2.6rem); margin-bottom: 1.5rem; line-height: 1.1; letter-spacing: -0.04em;">Platform Suite<br>Neural-Powered<br>Infrastructure</div>
              <div class="bc-tx" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5;">A complete system of smart products that transform how infrastructure thinks, learns, and evolves.</div>
              <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; width: 100%; max-width: 200px; margin: 3rem 0; opacity: 0.8;">
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #fff;"></div>
              </div>
            </div>
            
            <div style="margin-top: auto; display: flex; align-items: center; gap: 0.8rem; font-size: 0.85rem; font-weight: 500;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" /><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" /></svg>
              Neural intelligence inside
            </div>
          </div>
        </div>
        
        <div class="bc rvs">
          <div class="bc-img" style="background: linear-gradient(135deg, #1f1f1f, #151515);">[ AI DNA UI ]</div>
          <div class="bc-grid-icon">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div class="bc-content">
            <div class="bc-head" style="max-width: 100%;">
              <div class="bc-tt" style="font-size: 1.4rem;">Design Engine</div>
            </div>
          </div>
          <div class="bc-cta-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg></div>
        </div>
        
        <div class="bc rvs">
          <div class="bc-img" style="background: linear-gradient(135deg, #222, #181818);">[ Swipe File UI ]</div>
          <div class="bc-grid-icon">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div class="bc-content">
            <div class="bc-head" style="max-width: 100%;">
              <div class="bc-tt" style="font-size: 1.4rem;">Scale Matrix</div>
            </div>
          </div>
          <div class="bc-cta-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg></div>
        </div>
        
        <div class="bc rvs">
          <div class="bc-img" style="background: linear-gradient(135deg, #1c1c1c, #111);">[ Visual Search UI ]</div>
          <div class="bc-grid-icon">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div class="bc-content">
            <div class="bc-head" style="max-width: 100%;">
              <div class="bc-tt" style="font-size: 1.4rem;">Neural Net</div>
            </div>
          </div>
          <div class="bc-cta-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg></div>
        </div>
        
        <div class="bc rvs">
          <div class="bc-img" style="background: linear-gradient(135deg, #1a1a1a, #0f0f0f);">[ Tagging UI ]</div>
          <div class="bc-grid-icon">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
          </div>
          <div class="bc-content">
            <div class="bc-head" style="max-width: 100%;">
              <div class="bc-tt" style="font-size: 1.4rem;">Shield Core</div>
            </div>
          </div>
          <div class="bc-cta-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg></div>
        </div>
        
        <div class="bc rvs" style="display: flex; align-items: center; justify-content: center; background: #0c0c0c; border: 1px solid var(--color-border);">
          <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="1.5">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
          </svg>
        </div>
        
        <div class="bc rvs" style="background: #111; padding: 2.5rem;">
          <div class="bc-content" style="justify-content: space-between;">
            <div>
              <div class="bc-tt" style="font-size: 1.8rem; margin-bottom: 0.5rem; font-weight: 500;">Neural Core <span style="color: var(--color-text-tertiary); font-weight: 400; font-size: 1.5rem;">4.0b</span></div>
              <div style="color: var(--color-primary); font-size: 0.85rem; font-weight: 400;">Early beta access now available.</div>
            </div>
            
            <div style="margin-top: 5rem; margin-bottom: 3rem;">
              <div style="font-size: 0.65rem; color: var(--color-text-tertiary); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; display: inline-block; background: var(--color-border); padding: 0.2rem 0.5rem; border-radius: 4px;">Development Progress</div>
              <div style="font-size: 4rem; font-weight: 300; letter-spacing: -0.04em;">84.7<span style="font-size: 1.8rem; color: var(--color-text-tertiary);">%</span></div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
              <div style="font-size: 0.9rem; color: var(--color-text-secondary);">Join early beta</div>
              <div class="bc-cta-btn" style="position: static; margin: 0; width: 44px; height: 44px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
            </div>
          </div>
        </div>
      </div>
"""

new_content = pre_content + start_marker + new_grid + end_marker + post_content

with open('index.html', 'w') as f:
    f.write(new_content)

print("Updated grid successfully.")
