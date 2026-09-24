"""
20-Slide Professional PowerPoint Deck Generator
Matches Section 39 (Final Presentation Compatibility) of the Master Prompt
Program: AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen slides (13.33 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Professional Color Palette
    NAVY = RGBColor(26, 54, 93)       # #1A365D - Dominant dark
    SLATE = RGBColor(43, 108, 176)     # #2B6CB0 - Accent blue
    CHARCOAL = RGBColor(45, 55, 72)    # #2D3748 - Body text
    MUTED = RGBColor(113, 128, 150)    # #718096 - Subtitles
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(247, 250, 252) # #F7FAFC - Card backgrounds
    BORDER_COL = RGBColor(226, 232, 240)

    def add_header(slide, title_text, category="AICTE | IBM SKILLSBUILD INTERNSHIP 2026"):
        # Top banner / tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.4))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = SLATE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = NAVY

    def add_card(slide, left, top, width, height, bg_color=LIGHT_BG):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = BORDER_COL
        shape.line.width = Pt(1)
        return shape

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "AICTE | IBM SKILLSBUILD INTERNSHIP 2026  •  BHARATCARES"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(144, 205, 244)
    p0.space_after = Pt(20)

    p1 = tf.add_paragraph()
    p1.text = "AI-Powered E-Commerce Customer Segmentation\n& Sales Intelligence"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.space_after = Pt(20)

    p2 = tf.add_paragraph()
    p2.text = "Comprehensive Transactional Analytics on the Brazilian Olist E-Commerce Dataset"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_after = Pt(40)

    p3 = tf.add_paragraph()
    p3.text = "Student Name: Anurag Ranjan   |   Environment: Google Colab & Python   |   AI Assistant: Google Gemini"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(203, 213, 225)

    # ==========================================
    # SLIDE 2: Executive Summary
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Slide 2: Executive Summary")
    
    kpis = [
        ("BRL 1.15M", "Peak Monthly Sales", "November 2017 driven by Black Friday"),
        ("Health & Beauty", "Top Category", "BRL 1.41M in delivered sales value"),
        ("1.92x Spend", "Repeat vs One-time", "BRL 308.53 vs BRL 160.73 average"),
        ("37.4% Share", "São Paulo Dominance", "BRL 5.77M delivered in SP alone")
    ]
    for i, (metric, label, desc) in enumerate(kpis):
        left = Inches(0.8 + i * 2.95)
        add_card(s2, left, Inches(1.8), Inches(2.8), Inches(1.8))
        tb = s2.shapes.add_textbox(left + Inches(0.15), Inches(1.9), Inches(2.5), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p_m = tf.paragraphs[0]
        p_m.text = metric
        p_m.font.size = Pt(18)
        p_m.font.bold = True
        p_m.font.color.rgb = NAVY
        p_l = tf.add_paragraph()
        p_l.text = label
        p_l.font.size = Pt(11)
        p_l.font.bold = True
        p_l.font.color.rgb = SLATE
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = CHARCOAL

    # Summary narrative card
    add_card(s2, Inches(0.8), Inches(4.0), Inches(11.65), Inches(2.6))
    tb_narr = s2.shapes.add_textbox(Inches(1.1), Inches(4.2), Inches(11.1), Inches(2.2))
    tf_narr = tb_narr.text_frame
    tf_narr.word_wrap = True
    p = tf_narr.paragraphs[0]
    p.text = "Analytical Highlights & Strategic Summary:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_after = Pt(8)

    bullets = [
        "Delivered Transaction Baseline: Synthesized 110,197 delivered records across 93,358 unique customers and 27 Brazilian states.",
        "Revenue Definition: Delivered Sales Value = Product Price + Freight Value (captures full platform gross expenditure).",
        "High-Value Concentration: Median-threshold segmentation revealed High-Value customers drive 80.8% of platform revenue (4.22x multiple).",
        "AI Co-pilot Workflow: Google Gemini provided algorithmic support, visualization guidance, and statistical structure validated by Python."
    ]
    for b in bullets:
        pb = tf_narr.add_paragraph()
        pb.text = f"•  {b}"
        pb.font.size = Pt(10.5)
        pb.font.color.rgb = CHARCOAL
        pb.space_after = Pt(4)

    # Helper function for 2-column or content slides
    def build_content_slide(slide_num, title, left_title, left_bullets, right_title, right_bullets):
        slide = prs.slides.add_slide(blank_layout)
        add_header(slide, f"Slide {slide_num}: {title}")
        
        # Left card
        add_card(slide, Inches(0.8), Inches(1.8), Inches(5.65), Inches(5.0))
        tb_l = slide.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.05), Inches(4.5))
        tf_l = tb_l.text_frame
        tf_l.word_wrap = True
        p_lt = tf_l.paragraphs[0]
        p_lt.text = left_title
        p_lt.font.size = Pt(14)
        p_lt.font.bold = True
        p_lt.font.color.rgb = NAVY
        p_lt.space_after = Pt(10)
        for b in left_bullets:
            pb = tf_l.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = CHARCOAL
            pb.space_after = Pt(6)

        # Right card
        add_card(slide, Inches(6.8), Inches(1.8), Inches(5.65), Inches(5.0))
        tb_r = slide.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.05), Inches(4.5))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        p_rt = tf_r.paragraphs[0]
        p_rt.text = right_title
        p_rt.font.size = Pt(14)
        p_rt.font.bold = True
        p_rt.font.color.rgb = NAVY
        p_rt.space_after = Pt(10)
        for b in right_bullets:
            pb = tf_r.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = CHARCOAL
            pb.space_after = Pt(6)
        return slide

    # SLIDE 3: Problem Statement & Objectives
    build_content_slide(
        3, "Problem Statement & Business Objectives",
        "Core Industry Challenges",
        [
            "High Customer Acquisition vs. Low Retention: 97% of e-commerce buyers make only a single purchase, capping Customer Lifetime Value.",
            "Demand Seasonality Surges: Monthly revenue volatility causes inventory and logistics bottlenecks without data forecasting.",
            "Skewed Category Contribution: Unclear visibility into which product categories attract high-value repeat spenders.",
            "Geographic Concentration: Over 60% of sales concentrated in Southeast Brazil, requiring localized logistics optimization."
        ],
        "Key Project Objectives",
        [
            "O1: Quantify monthly and annual delivered sales trends and seasonal growth.",
            "O2: Rank product categories by delivered sales value and isolate primary drivers.",
            "O3: Profile one-time vs. repeat customer purchasing behavior.",
            "O4: Construct a 4-quadrant behavioral customer segmentation model.",
            "O5: Map regional market share across all 27 Brazilian states.",
            "O6: Conduct inferential statistical hypothesis testing (Welch's t-test)."
        ]
    )

    # SLIDE 4: Dataset Overview
    build_content_slide(
        4, "Dataset Overview (Olist E-Commerce)",
        "Olist Relational Dataset Architecture",
        [
            "Source: Kaggle Brazilian E-Commerce Public Dataset by Olist.",
            "Scope: 100,000+ anonymized orders from 2016 to 2018 across Brazilian marketplaces.",
            "Target Schema: Relational multi-table structure linking transactional events, line items, customers, products, and categories.",
            "Focused Scope: Utilized 5 core tables directly relevant to revenue, product, and customer analytics."
        ],
        "Primary Relational Tables Used",
        [
            "olist_orders_dataset.csv: 99,441 orders with timestamps and delivery status.",
            "olist_order_items_dataset.csv: 112,650 line items with prices and freight charges.",
            "olist_customers_dataset.csv: Maps order instances to unique customer identities and states.",
            "olist_products_dataset.csv: Catalog of 32,951 products with dimensions and categories.",
            "product_category_name_translation.csv: Standard English translation dictionary."
        ]
    )

    # SLIDE 5: Data Preparation & Cleaning
    build_content_slide(
        5, "Data Preparation & Cleaning",
        "Rigorous Cleaning Methodology",
        [
            "Standardized Datetime Conversion: Converted 5 timestamp fields to Pandas datetime objects for accurate temporal aggregation.",
            "Category Translation Alignment: Merged product table with translation dictionary on product_category_name.",
            "No Silent Record Deletion: Preserved all legitimate commercial records; imputed 1,559 missing English categories with 'unknown' (1.41%).",
            "Data Validation: Verified numeric datatypes and confirmed zero negative values in price and freight."
        ],
        "Quality Audit Metrics",
        [
            "Pre-cleaning Missing Values: Audited all tables; missing values strictly isolated to optional delivery timestamps and product metadata.",
            "Audit Summary: 0 duplicate rows across primary identifier keys.",
            "Delivered Records Preserved: 110,197 line items preserved post-cleaning.",
            "Reproducibility: Configurable DATA_PATH compatible with Google Colab and local environments."
        ]
    )

    # SLIDE 6: Data Integration & Feature Engineering
    build_content_slide(
        6, "Data Integration & Feature Engineering",
        "Star-Relational Data Join",
        [
            "Orders ──[inner join]──> Customers on customer_id (preserves customer_unique_id).",
            "Orders ──[inner join]──> Order Items on order_id (captures price and freight per item).",
            "Order Items ──[left join]──> Products Cleaned on product_id (attaches English category).",
            "Delivered Filter: Focused strictly on order_status == 'delivered' (97.02% of orders) for verified revenue."
        ],
        "Engineered Analytical Features",
        [
            "sales_value = price + freight_value: Reflects total realized customer expenditure.",
            "Temporal Extractors: year, month, month_name, year_month period for trend analysis.",
            "customer_type: One-time (1 order) vs Repeat (> 1 order) at unique customer level.",
            "value_tier: High-Value (>= BRL 89.81 median) vs Low-Value (< median)."
        ]
    )

    # SLIDE 7: Business Questions
    build_content_slide(
        7, "Business Questions Addressed",
        "Strategic Analytical Inquiry",
        [
            "BQ 1 (Sales Analysis): How does delivered sales value trend over time, and what periods record peak commercial performance?",
            "BQ 2 (Category Analysis): Which product categories drive the highest delivered sales value across the platform?",
            "BQ 3 (Customer Behavior): What is the commercial and volume difference between one-time and repeat customers?"
        ],
        "Geographic & Cohort Inquiry",
        [
            "BQ 4 (Geographic Distribution): Which Brazilian states generate the highest delivered sales value and how concentrated is demand?",
            "BQ 5 (Customer + Product Affinity): Which product categories contribute most to the spending of High-Value Repeat customers?"
        ]
    )

    # SLIDE 8: Exploratory Data Analysis
    build_content_slide(
        8, "Exploratory Data Analysis (EDA)",
        "Delivered Orders Baseline",
        [
            "Delivered Records: 110,197 line items representing 96,478 unique completed orders.",
            "Customer Reach: 93,358 distinct individual buyers (customer_unique_id).",
            "Total Delivered Sales: BRL 15,419,773.75 across the observation period.",
            "Order Status Distribution: Delivered orders represent 97.02% of total platform volume."
        ],
        "Metric Distribution Overview",
        [
            "Average Line-Item Value: BRL 140.88 (std: BRL 215.70).",
            "Median Line-Item Value: BRL 86.80 (reflects healthy right-skewed commercial distribution).",
            "Average Freight Value: BRL 19.99 (~14.2% of total item transaction value).",
            "Non-delivered Exclusions: Shipped (1.11%), Canceled (0.63%), Unavailable (0.61%)."
        ]
    )

    # SLIDE 9: Monthly Sales Analysis
    build_content_slide(
        9, "Monthly Sales Analysis (BQ 1)",
        "Temporal Sales Dynamics",
        [
            "Peak Month: November 2017 generated BRL 1,153,364.20 in delivered sales value.",
            "Driver: Nationwide Brazilian Black Friday promotional surge.",
            "Lowest Observed Month: December 2016 (BRL 19.62) due to initial platform pilot phase.",
            "2018 Steady State: Monthly sales stabilized between BRL 850K and BRL 1.05M."
        ],
        "Year-over-Year Trajectory",
        [
            "2016 Delivered Revenue: BRL 46,653.74 (partial operational inception).",
            "2017 Delivered Revenue: BRL 6,921,535.24 (+14,735% operational expansion).",
            "2018 Delivered Revenue: BRL 8,451,584.77 (+22.11% YoY commercial growth).",
            "Chart: Vis 1 Line chart with peak callout annotation saved in outputs/figures/."
        ]
    )

    # SLIDE 10: Product Category Analysis
    build_content_slide(
        10, "Product Category Analysis (BQ 2)",
        "Top Category Leaders (BRL)",
        [
            "1. Health & Beauty: BRL 1,412,089.53 (9,670 items | 9.16% share)",
            "2. Watches & Gifts: BRL 1,305,541.61 (5,991 items | 8.47% share)",
            "3. Bed Bath & Table: BRL 1,241,681.72 (11,115 items | 8.05% share)",
            "4. Sports & Leisure: BRL 1,156,656.48 (8,641 items | 7.50% share)",
            "5. Computers & Accessories: BRL 1,059,272.40 (7,827 items | 6.87% share)"
        ],
        "Category Insights",
        [
            "Concentration: Top 5 categories represent ~40.0% of all delivered revenue.",
            "Top 10 categories account for over 65% of platform sales.",
            "Catalog Breadth: 71 distinct product categories actively transacted.",
            "Chart: Vis 2 Horizontal bar chart highlighting Top 10 categories."
        ]
    )

    # SLIDE 11: Customer Analysis
    build_content_slide(
        11, "Customer Purchasing Behavior (BQ 3)",
        "One-Time vs. Repeat Breakdown",
        [
            "Total Unique Customers: 93,358 distinct buyers.",
            "One-Time Customers: 90,557 buyers (97.00% of customer base).",
            "Repeat Customers: 2,801 buyers (3.00% of customer base).",
            "Total Orders Generated: Repeat buyers placed 5,921 orders (2.11 orders/customer average)."
        ],
        "Monetary Value Comparison",
        [
            "One-Time Customer Average Sales: BRL 160.73 per customer.",
            "Repeat Customer Average Sales: BRL 308.53 per customer.",
            "Value Premium: Repeat customers generate 1.92x the sales value of one-time buyers.",
            "Chart: Vis 3 Bar chart comparing average sales per customer type."
        ]
    )

    # SLIDE 12: Geographic Analysis
    build_content_slide(
        12, "Geographic Analysis (BQ 4)",
        "Top State Performance",
        [
            "1. São Paulo (SP): BRL 5,769,703.15 (40,494 orders | 37.42% share)",
            "2. Rio de Janeiro (RJ): BRL 2,055,401.57 (12,350 orders | 13.33% share)",
            "3. Minas Gerais (MG): BRL 1,818,891.67 (11,355 orders | 11.80% share)",
            "4. Rio Grande do Sul (RS): BRL 861,472.79 (5,342 orders | 5.59% share)",
            "5. Paraná (PR): BRL 781,708.80 (4,923 orders | 5.07% share)"
        ],
        "Spatial Concentration Insights",
        [
            "Southeast Cluster: SP, RJ, and MG together account for 62.55% of all national sales.",
            "Lowest Sales State: Roraima (RR) at BRL 9,039.52.",
            "Multiple: SP generates 638x the delivered sales value of RR.",
            "Interpretation: Reflects urbanization and logistics networks, not marketing failure."
        ]
    )

    # SLIDE 13: Customer Segmentation
    build_content_slide(
        13, "Customer Segmentation (4 Behavioral Quadrants)",
        "Segmentation Matrix (Median = BRL 89.81)",
        [
            "High-Value One-time: 44,310 customers (47.46%) | BRL 11,626,953.48 (75.40% share) | Avg: BRL 262.40",
            "Low-Value One-time: 46,247 customers (49.54%) | BRL 2,928,632.81 (19.00% share) | Avg: BRL 63.33",
            "High-Value Repeat: 2,467 customers (2.64%) | BRL 836,632.50 (5.43% share) | Avg: BRL 339.13",
            "Low-Value Repeat: 334 customers (0.36%) | BRL 27,554.96 (0.18% share) | Avg: BRL 82.50"
        ],
        "Strategic Cohort Focus",
        [
            "High-Value One-time represents 75.4% of total platform sales: Primary candidate for retention campaigns.",
            "High-Value Repeat boasts the highest average revenue (BRL 339.13): Platform advocates.",
            "Low-Value One-time comprises 49.5% of users but under 19% of sales: Price-sensitive discount seekers.",
            "Clear, reproducible median threshold documented."
        ]
    )

    # SLIDE 14: Key Observations
    build_content_slide(
        14, "Key Observations (Dynamically Calculated)",
        "Empirical Findings 1 & 2",
        [
            "Observation 1 (Peak Month): November 2017 recorded the highest monthly delivered sales value at BRL 1,153,364.20.",
            "Observation 2 (Top Category): Health & Beauty was the highest-selling product category by delivered sales value at BRL 1,412,089.53."
        ],
        "Empirical Findings 3, 4 & 5",
        [
            "Observation 3 (Customer Spend): Repeat customers had a higher average delivered sales value per customer than one-time customers (BRL 308.53 vs BRL 160.73).",
            "Observation 4 (Top Geography): São Paulo recorded the highest delivered sales value among Brazilian states at BRL 5,769,703.15.",
            "Observation 5 (Value Skew): High-value customers generated substantially more delivered sales value than low-value customers (BRL 12.46M vs BRL 2.96M)."
        ]
    )

    # SLIDE 15: Business Insights
    build_content_slide(
        15, "Business Insights",
        "Commercial & Behavioral Insights",
        [
            "Insight 1 (Seasonal Surges): November 2017 showed the strongest monthly sales, proving Black Friday is the dominant commercial driver in Brazil.",
            "Insight 2 (Category Leadership): Health & Beauty generates high ticket size and steady demand, making it an anchor category for promotional campaigns.",
            "Insight 3 (Retention Premium): Repeat customers demonstrate a 1.92x spend premium, affirming that post-purchase retention drives substantial lifetime value."
        ],
        "Geographic & Value Insights",
        [
            "Insight 4 (Market Maturity): São Paulo's 37.4% market share highlights dense logistics infrastructure and high digital consumer adoption.",
            "Insight 5 (Value Concentration): High-value buyers generate over 80% of revenue, demanding dedicated VIP servicing and targeted merchandising."
        ]
    )

    # SLIDE 16: Hypothesis Testing
    build_content_slide(
        16, "Statistical Hypothesis Testing",
        "Hypothesis 1: Welch's Two-Sample t-test",
        [
            "H0: Mean sales value (Repeat) == Mean sales value (One-time).",
            "H1: Mean sales value (Repeat) > Mean sales value (One-time).",
            "Method: Welch's t-test (handles unequal variances & sample sizes: 2,801 vs 90,557).",
            "Result: t-statistic = 24.5016, p-value < 0.0001 (numerically approx. 0).",
            "Decision: Reject H0; statistically significant difference confirmed (empirical association, not causation)."
        ],
        "Hypotheses 2 & 3: Descriptive Tests",
        [
            "Hypothesis 2 (Revenue Contribution Ratio): High-Value cohort generated BRL 12.46M vs BRL 2.96M for Low-Value (4.22x ratio; descriptive benchmark).",
            "Hypothesis 3 (Spatial Distribution): Evaluated across 27 states (SP: BRL 5.77M vs RR: BRL 9.04K; descriptive spatial variance)."
        ]
    )

    # SLIDE 17: Business Recommendations
    build_content_slide(
        17, "Business Recommendations",
        "Actionable Strategic Roadmap",
        [
            "Recommendation 1: Customer Retention & Re-Engagement",
            "Target: 44,310 High-Value One-time buyers.",
            "Action: Trigger automated personalized email sequences 14–30 days post-delivery with category recommendations.",
            "Goal: Lift repeat purchase rate from 3.0% to 5.0% over 12 months."
        ],
        "Category & Logistics Strategies",
        [
            "Recommendation 2: Category Merchandising Optimization",
            "Action: Deepen supplier ties in top categories (Health & Beauty, Watches, Bed Bath) and bundle cross-category offerings.",
            "Recommendation 3: Regional Logistics Fulfillment Hubs",
            "Action: Partner with local 3PL micro-fulfillment centers in Greater São Paulo and Rio de Janeiro to reduce freight fees and delivery latency."
        ]
    )

    # SLIDE 18: AI Integration
    build_content_slide(
        18, "AI Integration (Google Gemini)",
        "AI-Assisted Analytics Workflow",
        [
            "Tool: Google Gemini in Google Colab environment.",
            "Role: Analytical co-pilot across the project lifecycle.",
            "Step 1: Formulating business questions and analytical queries.",
            "Step 2: Prompting Gemini for optimized Python & Pandas code.",
            "Step 3: Running code in Colab and verifying runtime accuracy."
        ],
        "Validation & Academic Rigor",
        [
            "Step 4: Independent calculation validation in Python.",
            "Step 5: Synthesizing statistical outputs into executive insights.",
            "Academic Integrity: AI assisted coding and structuring; all data metrics and p-values are empirical calculations from Olist data."
        ]
    )

    # SLIDE 19: Conclusion
    build_content_slide(
        19, "Project Conclusion",
        "Summary of Analytical Achievements",
        [
            "End-to-End Workflow: Successfully ingested, audited, cleaned, integrated, and analyzed 110,197 delivered records.",
            "Multi-Dimensional Intelligence: Addressed 5 core business questions spanning temporal, category, customer, and spatial dimensions.",
            "Scientific Rigor: Applied inferential Welch's t-test alongside median-based 4-quadrant behavioral segmentation."
        ],
        "Business Value Delivered",
        [
            "Defensible Evidence: Delivered actionable proof of repeat customer spend premiums and extreme geographic demand concentration.",
            "Operational Blueprints: Provided targeted retention, merchandising, and regional fulfillment roadmaps.",
            "Reproducibility: Fully documented, parameterized codebase runnable across Colab and local setups."
        ]
    )

    # SLIDE 20: Tools & Technologies
    build_content_slide(
        20, "Tools & Technologies",
        "Core Development Stack",
        [
            "Python 3.10+: Core data analytics and computational programming.",
            "Google Colab: Interactive cloud development and execution environment.",
            "Pandas: Data loading, multi-table relational joins, cleaning, and grouping.",
            "NumPy: Vectorized numerical processing and array calculations."
        ],
        "Visualization, Statistics & AI",
        [
            "Matplotlib: Custom publication-quality line and horizontal bar charts.",
            "SciPy (scipy.stats): Inferential statistical hypothesis testing (Welch's t-test).",
            "Google Gemini: AI-assisted analytical ideation, code synthesis, and insight drafting.",
            "python-docx & python-pptx: Programmatic report and presentation generation."
        ]
    )

    out_file = "Anurag_Ranjan_Presentation.pptx"
    prs.save(out_file)
    print(f"Presentation successfully created at: {os.path.abspath(out_file)}")

if __name__ == "__main__":
    create_presentation()
