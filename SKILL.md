---
name: company-research-team
description: |
  AI Multi-Agent Team Collaboration for Company Deep Research Analysis. Use this skill when researching and analyzing a company (such as listed companies, investment targets, business analysis, etc.).
  Applicable scenarios: (1) Research target company's business model (2) Analyze financial status (3) Evaluate industry competition landscape (4) Track technology evolution (5) Assess user experience (6) Interpret management team (7) Review historical performance (8) Analyze macro environment impact
  Workflow: Create Team → Assign Tasks → Independent Analysis → Cross-domain Discussion → Integrate Conclusions
  Optional: Enable Tushare for Chinese listed companies to get real-time financial data
---

# Company Research Team (Company Research Team)

Use multi-agent team for in-depth research and analysis of target companies.

## Quick Start

### 1. Create Research Team

```python
TeamCreate(
    agent_type="general-purpose",
    description="Research and analyze [Company Name], 8 professional analysts conducting deep analysis from different dimensions",
    team_name="[company-name]-research"
)
```

### 2. Define Analyst Roles

Create 8 specialized analyst Tasks:

| # | Role | Analysis Dimension |
|----|------|-------------------|
| 1 | Business Model Analyst | Business model, business loop, profit model |
| 2 | Financial Report Analyst | Three statements analysis, cash flow, profitability |
| 3 | Industry Competition Analyst | Porter's Five Forces, industry chain, competitors |
| 4 | Macro Environment Analyst | Policy environment, economic cycle, industry trends |
| 5 | Technology Evolution Tracker | Technology roadmap, R&D investment, patent portfolio |
| 6 | User Value Experience Officer | User reputation, NPS, product experience |
| 7 | Management Behavior Interpreter | Ownership structure, decision-making style, strategic capability |
| 8 | Historical Review Researcher | Major events, turning points, rise and fall logic |

### 3. Assign Research Tasks

Use Task tool to assign tasks to each analyst, containing:
- Analysis dimensions and question lists
- Data sources (financial reports, news, research reports, etc.)
- Output requirements (independent viewpoints + HTML PPT)

### 4. Cross-domain Discussion

When all analysts complete preliminary analysis, organize cross-dimensional discussion:
- Find consensus points
- Discover contradiction points
- Ask key questions about contradictions

### 5. Integrate Conclusions

Create comprehensive analysis report integrating all dimensional viewpoints.

## Detailed Workflow

### Phase 1: Team Initialization

1. Create Team, set team_name
2. Create 8 Tasks (corresponding to 8 analysts)
3. Spawn 8 Agents and assign tasks

### Phase 2: Independent Analysis

Each analyst needs to:
1. Search public information (financial reports, news, research reports)
2. Analyze from professional perspective
3. Draw independent, profound conclusions
4. Create HTML PPT to display analysis results
5. Save PPT to working directory

### Phase 3: Cross-domain Discussion

Organize 3 rounds of discussion:
1. **Preliminary comparison**: Compare conclusions across analysts
2. **Deep inquiry**: Ask questions about contradiction points
3. **Core collision**: In-depth debate on key contradictions

### Phase 4: Integration Output

Create comprehensive analysis document:
- Core data summary
- Eight-dimensional analysis summary
- Cross-dimensional discussion conclusions
- Core contradictions and consensus

## Data Sources

- **Financial Data**: Sina Finance, Yahoo Finance, Company Annual Reports
- **Industry Data**: Industry Associations, Third-party Research Reports
- **User Feedback**: Social Media, Autohome, DongcheDi
- **News**: Public media reports

### Tushare 数据 (可选)

对于中国A股上市公司，可以启用Tushare获取更精准的财务数据：

**配置方法：**
1. 安装Tushare: `pip install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple`
2. 在 [Tushare.pro](https://tushare.pro/register) 注册获取token
3. 设置环境变量: `export TUSHARE_TOKEN=your_token`

**可用数据：**
| 数据类型 | 接口 | 说明 |
|----------|------|------|
| 股票行情 | daily, daily_basic | 每日OHLCV、PE、PB等 |
| 财务报表 | income, balancesheet, cashflow | 季报/年报数据 |
| 财务指标 | fina_indicator | ROE、ROA、毛利率等 |
| 融资融券 | margin | 融资融券数据 |
| 资金流向 | moneyflow | 主力资金流向 |
| 宏观数据 | cn_gdp, cn_cpi, cn_pmi, shibor | GDP、CPI、利率等 |
| 股东数据 | top10_holders, stk_managers | 股东结构、管理层 |

## Output Requirements

### Independent Analysis Report

Each analyst needs to generate:
1. **Markdown Analysis Document**: Detailed analysis
2. **HTML PPT Presentation**: Visual display (8-10 slides)

### Comprehensive Report

Team generates:
1. **Markdown Comprehensive Report**: Complete analysis document
2. **HTML Comprehensive PPT**: Core conclusions presentation (10 slides)

## Key Principles

1. **Independent Viewpoints**: Each analyst must draw their own independent conclusions
2. **Data-driven**: All conclusions must be supported by data
3. **Cross-domain Dialogue**: Different dimensional viewpoints collide to generate insights
4. **Visual Presentation**: HTML PPT for easy display and sharing

## Common Company Research Scenarios

- Listed company financial report analysis
- Investment target due diligence
- In-depth competitor analysis
- Industry trend research
- Startup evaluation
