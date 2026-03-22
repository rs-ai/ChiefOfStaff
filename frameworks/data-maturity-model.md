# Data Maturity Model

## The 5 Levels

### Level 1: Ad-Hoc
**Characteristics**: Data work is reactive and inconsistent. Individuals have their own spreadsheets. No shared definitions. "Data" means someone emails an Excel file.

- **Tools**: Excel, email, shared drives, maybe a basic BI tool nobody trusts
- **Team**: No dedicated data roles — analysts are embedded and self-taught
- **Governance**: None. Everyone has their own version of the truth
- **Decision-making**: Gut feel supplemented by whoever can pull numbers fastest

### Level 2: Reactive
**Characteristics**: A small data team exists but spends 80%+ of time on ad-hoc requests. Some dashboards exist but break regularly. Data quality issues are known but not systematically addressed.

- **Tools**: BI platform (Tableau/Power BI), basic SQL access, some Python scripts
- **Team**: 2-5 analysts, possibly a data engineer. No clear career path
- **Governance**: Informal — the senior analyst is the de facto data steward
- **Decision-making**: Data-informed for some decisions, but trust is inconsistent

### Level 3: Defined
**Characteristics**: Documented data models, defined KPIs, reliable pipelines. Data team has a roadmap, not just a request queue. Self-service analytics emerging.

- **Tools**: Cloud data warehouse, dbt or equivalent, orchestration (Airflow), governed BI layer
- **Team**: 8-15 people across analytics, engineering, and possibly ML. Clear roles and career paths
- **Governance**: Data catalog exists, ownership assigned, quality checks automated
- **Decision-making**: Most operational decisions are data-driven. Strategic decisions increasingly so

### Level 4: Managed
**Characteristics**: Data is a product, not a service. Platform thinking. Proactive insights, not just reactive reporting. ML models in production.

- **Tools**: Modern data stack fully implemented, feature stores, ML platforms, data contracts
- **Team**: 15-30+ with specialization: analytics engineering, ML engineering, data product management
- **Governance**: Formal data governance board, privacy by design, automated compliance
- **Decision-making**: Data-driven by default. Experiments and A/B testing are standard practice

### Level 5: Optimized
**Characteristics**: Data and AI are embedded in every business process. Continuous improvement loops. The data team enables the entire org, not just serves it.

- **Tools**: Full platform with self-service ML, real-time analytics, automated decision systems
- **Team**: Federated model — central platform team + embedded data professionals in every function
- **Governance**: Automated, policy-as-code, real-time data quality monitoring
- **Decision-making**: AI-augmented decisions are the norm. Human judgment applied to exceptions

## Assessment Template

Rate each function/team on the 5 levels across these dimensions:

| Dimension | Sales | Marketing | Finance | Operations | Product | HR |
|-----------|-------|-----------|---------|------------|---------|-----|
| Data accessibility | | | | | | |
| Data quality | | | | | | |
| Analytics capability | | | | | | |
| Tool maturity | | | | | | |
| Governance | | | | | | |
| Data literacy | | | | | | |
| **Average** | | | | | | |

## Advancement Playbook

### Level 1 to 2: Establish the Foundation
- **Hire**: First dedicated data analyst or engineer
- **Quick win**: Build one trusted dashboard for one high-visibility metric
- **Action**: Audit existing data sources; create a basic inventory
- **Timeline**: 3-6 months
- **Biggest risk**: Trying to boil the ocean. Pick one domain and get it right.

### Level 2 to 3: Professionalize
- **Hire**: Analytics engineers, a data engineering lead
- **Quick win**: Implement a cloud data warehouse, eliminate the worst spreadsheet workflows
- **Action**: Define core metrics, build a data model, implement testing
- **Timeline**: 6-12 months
- **Biggest risk**: Building infrastructure without business alignment. Every pipeline should trace to a business question.

### Level 3 to 4: Productize
- **Hire**: ML engineers, data product managers
- **Quick win**: Deploy first ML model to production with measurable business impact
- **Action**: Implement data contracts, build a feature store, establish an experimentation platform
- **Timeline**: 12-18 months
- **Biggest risk**: Technology-first thinking. The org needs to be ready for ML outputs, not just the tech stack.

### Level 4 to 5: Embed and Scale
- **Hire**: Shift to a federated model — embed data professionals in business units
- **Quick win**: Automate a decision process end-to-end with AI
- **Action**: Implement data mesh or equivalent decentralized model with central governance
- **Timeline**: 18-24 months
- **Biggest risk**: Losing coherence. Decentralization without governance creates chaos.

## Key Principle

**You can't skip levels.** Trying to build ML models (Level 4) when your data quality is Level 1 will fail. Meet the organization where it is, not where you wish it was. Advance one level at a time, prove value, then move up.
