// ── VEGA-LITE EMBED OPTIONS ──────────────────────────────────
const OPT     = { actions: false, renderer: "svg"    };
const OPT_CVS = { actions: false, renderer: "canvas" };

// ── ACT 1: SCALE & VALUE ─────────────────────────────────────
vegaEmbed('#vis1', 'vis1_map.json',           OPT).catch(console.error);
vegaEmbed('#vis2', 'vis2_stacked_bar.json',   OPT).catch(console.error);
vegaEmbed('#vis3', 'vis3_waffle.json',        OPT).catch(console.error);

// ── ACT 2: ENVIRONMENTAL STRESSORS ───────────────────────────
vegaEmbed('#vis4', 'vis4_thermal_map.json',         OPT).catch(console.error);
vegaEmbed('#vis5', 'vis5_bleaching_severity.json',  OPT).catch(console.error);
// vis6: vconcat with container width needs canvas renderer to fill the div
vegaEmbed('#vis6', 'vis6_interactive_dashboard.json', OPT_CVS).catch(console.error);

// ── ACT 3: SHIFTING BASELINES & DAMAGE ───────────────────────
vegaEmbed('#vis7', 'vis7_treemap.json',       OPT).catch(console.error);
vegaEmbed('#vis8', 'vis8_diverging_bar.json', OPT).catch(console.error);
vegaEmbed('#vis9', 'vis9_cyclone_map.json',   OPT).catch(console.error);

// ── ACT 4: CONSERVATION OUTCOMES ─────────────────────────────
vegaEmbed('#vis10', 'vis10_slope_graph.json', OPT).catch(console.error);
vegaEmbed('#vis11', 'vis11_heatmap.json',     OPT).catch(console.error);

// ── SCROLL ANIMATION ─────────────────────────────────────────
window.addEventListener('load', function () {
    const acts = document.querySelectorAll('.act');
    setTimeout(() => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    entry.target.classList.remove('animate');
                }
            });
        }, { threshold: 0.05 });

        acts.forEach(act => {
            const rect = act.getBoundingClientRect();
            if (rect.top > window.innerHeight) {
                act.classList.add('animate');
            }
            observer.observe(act);
        });
    }, 800);
});