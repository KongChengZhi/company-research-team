# HTML PPT Templates & Style Guide

## Slide Structure Recommendation

Each analysis report should have 8-10 slides:

### Cover Slide
- Company Name
- Report Title (Analysis Dimension)
- Analyst Name
- Date

### Data Overview Slide
- Core financial/operating data
- Key metric cards

### Analysis Content Slides (4-6 slides)
- One core theme per slide
- Use card-based layout
- Data visualization

### Comparison Slide (if applicable)
- Comparison with competitors
- Use tables for display

### Conclusion Slide
- Core viewpoint summary
- Risk warnings
- Recommendations

## Color Scheme Reference

### Tech Style (Dark Background)
```css
body {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    color: #fff;
}
h1, h2 { color: #00d4ff; }
.card { background: rgba(255,255,255,0.05); }
```

### Business Style (Light Background)
```css
body {
    background: #f5f5f5;
    color: #333;
}
h1, h2 { color: #2c3e50; }
.card { background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
```

### Brand Colors
- Blue: #007bff, #00d4ff
- Green: #00ff88, #2ecc71
- Purple: #7b2ff7, #9b59b6
- Red: #ff6b6b, #e74c3c

## Common Component Styles

### Metric Card
```css
.stat-box {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
}
.stat-number {
    font-size: 42px;
    font-weight: bold;
    color: #00ff88;
}
```

### Data Table
```css
.table {
    width: 100%;
    border-collapse: collapse;
}
.table th {
    background: rgba(0,212,255,0.1);
    color: #00d4ff;
    padding: 15px;
    text-align: left;
}
.table td {
    padding: 15px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
```

### Navigation Dots
```css
.nav-dot {
    width: 12px;
    height: 12px;
    background: rgba(255,255,255,0.3);
    border-radius: 50%;
    cursor: pointer;
}
.nav-dot.active {
    background: #00d4ff;
    transform: scale(1.3);
}
```

### Conclusion Box
```css
.conclusion-box {
    background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(123,44,191,0.1));
    border: 2px solid #00d4ff;
    border-radius: 20px;
    padding: 40px;
}
```

## Interactive Features

### Keyboard Navigation
```javascript
document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') {
        if (cur < slides.length - 1) go(cur + 1);
    } else if (e.key === 'ArrowLeft') {
        if (cur > 0) go(cur - 1);
    }
});
```

### Touch Swipe
```javascript
document.addEventListener('touchstart', e => {
    touchStartX = e.touches[0].clientX;
});
document.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
        // Handle swipe
    }
});
```

## Output File Naming Convention

```
[Company Name][Analysis Dimension].html
Example:
- Li Auto Business Model Analysis.html
- Li Auto Porter Five Forces Analysis.html
- Li Auto Financial Analysis Report.html
```
