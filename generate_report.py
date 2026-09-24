"""
Professional DOCX Project Report Generator
Program: AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares
Project Title: AI-Powered E-Commerce Customer Segmentation & Sales Intelligence
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def style_heading(p, text, level=1):
    p.text = text
    p.paragraph_format.keep_with_next = True
    run = p.runs[0]
    run.font.name = 'Calibri'
    if level == 1:
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(26, 54, 93) # Deep Navy
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
    elif level == 2:
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(43, 108, 176) # Slate Blue
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
    elif level == 3:
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(45, 55, 72) # Charcoal
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)

def add_callout(doc, text, title="KEY TAKEAWAY:"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "EDF2F7") # Light slate grey
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run_t = p.add_run(f"{title} ")
    run_t.font.bold = True
    run_t.font.name = 'Calibri'
    run_t.font.size = Pt(10.5)
    run_t.font.color.rgb = RGBColor(26, 54, 93)
    
    run_body = p.add_run(text)
    run_body.font.name = 'Calibri'
    run_body.font.size = Pt(10)
    run_body.font.color.rgb = RGBColor(45, 55, 72)
    doc.add_paragraph() # Spacing

def format_table(table, header_bg="1A365D", alt_bg="F7FAFC"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Format header row
    for cell in table.rows[0].cells:
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.bold = True
                r.font.name = 'Calibri'
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(255, 255, 255)
    
    # Format data rows
    for i, row in enumerate(table.rows[1:], start=1):
        bg = alt_bg if i % 2 == 1 else "FFFFFF"
        for cell in row.cells:
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.name = 'Calibri'
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(45, 55, 72)

def generate_report():
    doc = Document()

    # Standard Margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Base body style configuration
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(45, 55, 72)

    # ==========================================
    # 1. COVER PAGE
    # ==========================================
    cover_p1 = doc.add_paragraph()
    cover_p1.paragraph_format.space_before = Pt(60)
    cover_p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = cover_p1.add_run("AICTE | IBM SkillsBuild Internship 2026\nBharatCares Technical Report\n")
    r_sub.font.size = Pt(13)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    cover_p2 = doc.add_paragraph()
    cover_p2.paragraph_format.space_before = Pt(30)
    cover_p2.paragraph_format.space_after = Pt(20)
    cover_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = cover_p2.add_run("AI-Powered E-Commerce Customer Segmentation\n& Sales Intelligence")
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(26, 54, 93)

    cover_p3 = doc.add_paragraph()
    cover_p3.paragraph_format.space_before = Pt(10)
    cover_p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_desc = cover_p3.add_run("An End-to-End Analytical Investigation of Transactional Dynamics,\nCustomer Value Quadrants, and Regional Revenue Patterns")
    r_desc.font.size = Pt(12)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(113, 128, 150)

    # Metadata table on cover page
    cover_table = doc.add_table(rows=6, cols=2)
    cover_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_info = [
        ("Candidate Name / Student ID:", "Anurag Ranjan"),
        ("Program Track:", "AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026"),
        ("Partner Organization:", "BharatCares"),
        ("Primary Dataset:", "Brazilian E-Commerce Public Dataset by Olist"),
        ("Data Repository Source:", "Kaggle (olistbr/brazilian-ecommerce)"),
        ("Analytical Technologies:", "Python, Pandas, NumPy, Matplotlib, SciPy, Google Gemini")
    ]
    for idx, (label, val) in enumerate(meta_info):
        row = cover_table.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.paragraphs[0].text = label
        cell_lbl.paragraphs[0].runs[0].font.bold = True
        cell_lbl.paragraphs[0].runs[0].font.size = Pt(10)
        cell_lbl.paragraphs[0].runs[0].font.color.rgb = RGBColor(26, 54, 93)
        cell_val.paragraphs[0].text = val
        cell_val.paragraphs[0].runs[0].font.size = Pt(10)
        set_cell_margins(cell_lbl, top=60, bottom=60, left=80, right=80)
        set_cell_margins(cell_val, top=60, bottom=60, left=80, right=80)

    doc.add_page_break()

    # ==========================================
    # 2. EXECUTIVE SUMMARY
    # ==========================================
    style_heading(doc.add_paragraph(), "2. Executive Summary", level=1)
    doc.add_paragraph(
        "This project presents an AI-Powered E-Commerce Customer Segmentation & Sales Intelligence system "
        "using the Brazilian E-Commerce Public Dataset by Olist sourced from Kaggle. The study executes a "
        "comprehensive, reproducible analytics lifecycle encompassing multi-table relational integration, rigorous "
        "data cleaning and quality auditing, temporal feature engineering, exploratory data analysis, behavioral "
        "customer segmentation, and statistical hypothesis testing."
    )
    doc.add_paragraph(
        "The analytical baseline incorporates 110,197 delivered order-item records representing 93,358 unique customers "
        "across all 27 Brazilian states. Total delivered sales value is defined as the sum of item price and freight value, "
        "capturing true top-line consumer expenditure. Primary empirical findings reveal:"
    )
    
    findings_list = [
        "November 2017 recorded the platform's peak monthly delivered sales value of BRL 1,153,364.20, driven by Black Friday commercial surges.",
        "Health & Beauty achieved the highest category revenue at BRL 1,412,089.53, followed by Watches & Gifts and Bed Bath & Table.",
        "Repeat customers generated an average delivered sales value of BRL 308.53 compared to BRL 160.73 for one-time buyers (Welch's t = 24.5016, p < 0.001).",
        "São Paulo (SP) dominated regional sales with BRL 5,769,703.15 in delivered sales value (~37.3% national market share).",
        "A median-threshold segmentation revealed that High-Value customers contributed BRL 12,463,585.98 (80.8% of total delivered sales) versus BRL 2,956,187.77 for Low-Value customers (a 4.22x revenue ratio)."
    ]
    for item in findings_list:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(item)
        r.font.size = Pt(10.5)

    add_callout(
        doc,
        "All calculations were dynamically computed using Python, while Google Gemini was employed as an AI analytical assistant "
        "for algorithmic synthesis, methodology formulation, and narrative interpretation. Observational findings demonstrate strong "
        "empirical associations without inferring unvalidated causal mechanisms.",
        title="EXECUTIVE SUMMARY SYNTHESIS:"
    )

    # ==========================================
    # 3. PROBLEM STATEMENT
    # ==========================================
    style_heading(doc.add_paragraph(), "3. Problem Statement", level=1)
    doc.add_paragraph(
        "Modern online multi-vendor retail platforms generate vast streams of transactional records across distributed "
        "databases. However, raw operational data lacks immediate strategic clarity. E-commerce operators frequently struggle with:"
    )
    p_pts = [
        "Unpredictable Seasonal Fluctuations: Inability to anticipate monthly revenue swings leads to stock-outs or costly inventory surpluses.",
        "Customer Retention Blindspots: High customer acquisition costs (CAC) paired with an overwhelming majority of single-purchase buyers degrade customer lifetime value (LTV).",
        "Sub-optimal Merchandising: Lack of visibility into which specific product categories attract and retain high-value repeat buyers.",
        "Geographic Resource Misallocation: Over- or under-investing in logistics, fulfillment hubs, and regional marketing due to unquantified geographic sales concentration."
    ]
    for pt in p_pts:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.add_run(pt)

    # ==========================================
    # 4. BUSINESS OBJECTIVES
    # ==========================================
    style_heading(doc.add_paragraph(), "4. Business Objectives", level=1)
    doc.add_paragraph(
        "To resolve the aforementioned challenges, this project established eight quantifiable analytical goals:"
    )
    objectives = [
        ("O1: Longitudinal Sales Dynamics", "Quantify monthly and annual delivered sales trends, identify peak commercial windows, and interpret YoY trajectory."),
        ("O2: Product Hierarchy Intelligence", "Rank product categories by delivered sales value and isolate primary commercial drivers."),
        ("O3: Customer Behavioral Profiling", "Segment customers by order frequency (one-time vs. repeat) and compare average basket value."),
        ("O4: 4-Quadrant Segmentation", "Classify customers into High/Low Value and One-time/Repeat cohorts using an empirical median threshold."),
        ("O5: Spatial Market Mapping", "Assess delivered sales performance across all 27 Brazilian states to identify geographic concentration."),
        ("O6: Affinity Discovery", "Determine the top product categories driving repeat spend among high-value customer segments."),
        ("O7: Statistical Validation", "Conduct rigorous hypothesis testing (Welch's independent t-test) to validate customer spend differences."),
        ("O8: Actionable Recommendations", "Formulate targeted marketing, category management, and fulfillment strategies backed by verified data.")
    ]
    obj_table = doc.add_table(rows=len(objectives)+1, cols=2)
    obj_table.rows[0].cells[0].paragraphs[0].text = "Objective Code & Title"
    obj_table.rows[0].cells[1].paragraphs[0].text = "Scope & Description"
    for idx, (code_t, desc) in enumerate(objectives, start=1):
        obj_table.rows[idx].cells[0].paragraphs[0].text = code_t
        obj_table.rows[idx].cells[1].paragraphs[0].text = desc
    format_table(obj_table)

    # ==========================================
    # 5. DATASET OVERVIEW
    # ==========================================
    style_heading(doc.add_paragraph(), "5. Dataset Overview", level=1)
    doc.add_paragraph(
        "The project analyzes the Brazilian E-Commerce Public Dataset by Olist, hosted on Kaggle. "
        "The dataset documents real commercial transactions fulfilled across Brazilian marketplaces between 2016 and 2018."
    )
    dataset_schema = [
        ("olist_orders_dataset.csv", "Primary transactional log detailing order status (delivered, shipped, etc.) and all operational milestone timestamps."),
        ("olist_order_items_dataset.csv", "Line-item granular records specifying price, freight charges, product IDs, and merchant links per order."),
        ("olist_customers_dataset.csv", "Demographic table linking unique transaction instances (customer_id) to distinct individuals (customer_unique_id) and their location."),
        ("olist_products_dataset.csv", "Product catalog containing metadata, physical specifications, and category naming in native Portuguese."),
        ("product_category_name_translation.csv", "Relational dictionary providing standardized English translations for Portuguese category names.")
    ]
    ds_table = doc.add_table(rows=len(dataset_schema)+1, cols=2)
    ds_table.rows[0].cells[0].paragraphs[0].text = "Dataset Table Name"
    ds_table.rows[0].cells[1].paragraphs[0].text = "Analytical Role & Content"
    for idx, (tname, desc) in enumerate(dataset_schema, start=1):
        ds_table.rows[idx].cells[0].paragraphs[0].text = tname
        ds_table.rows[idx].cells[1].paragraphs[0].text = desc
    format_table(ds_table)

    # ==========================================
    # 6. DATA PREPARATION AND CLEANING
    # ==========================================
    style_heading(doc.add_paragraph(), "6. Data Preparation and Cleaning", level=1)
    doc.add_paragraph(
        "Data cleaning was executed systematically without silent data deletion. Specific transformations include:"
    )
    doc.add_paragraph(
        "1. Timestamp Standardization: All five temporal fields ('order_purchase_timestamp', 'order_approved_at', "
        "'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date') were converted "
        "from object strings to standardized Pandas datetime64 objects.",
        style='List Bullet'
    )
    doc.add_paragraph(
        "2. Category Translation & Null Imputation: Products catalog was merged with the translation dictionary. "
        "Unmatched or missing categories (1,559 records or 1.41% of line items) were imputed with 'unknown' to ensure no valid "
        "transaction was dropped while maintaining full auditability.",
        style='List Bullet'
    )
    doc.add_paragraph(
        "3. Numeric Verification: Price and freight fields were verified to ensure non-negative numeric floats.",
        style='List Bullet'
    )

    # ==========================================
    # 7. DATA INTEGRATION
    # ==========================================
    style_heading(doc.add_paragraph(), "7. Data Integration", level=1)
    doc.add_paragraph(
        "A star-like relational integration merged the five source tables. Orders was linked to Customers via 'customer_id' "
        "(inner join), then to Order Items via 'order_id' (inner join), and subsequently to the translated Products dataset "
        "via 'product_id' (left join)."
    )
    add_callout(
        doc,
        "Post-merge verification confirmed 110,197 delivered line-item records across 93,358 unique customers. "
        "Importantly, customer_unique_id was maintained as the primary unit of customer behavior to prevent multiple orders "
        "placed by the same person under different session IDs from skewing customer retention calculations.",
        title="INTEGRATION VALIDATION:"
    )

    # ==========================================
    # 8. FEATURE ENGINEERING
    # ==========================================
    style_heading(doc.add_paragraph(), "8. Feature Engineering", level=1)
    doc.add_paragraph(
        "To enable multidimensional business intelligence, several domain features were engineered:"
    )
    doc.add_paragraph(
        "• sales_value = price + freight_value: Reflects total delivered sales value generated per transaction line item. "
        "Summary statistics confirmed a mean of BRL 140.88 (std: BRL 215.70), median of BRL 86.80, and max of BRL 6,929.31.",
        style='List Bullet'
    )
    doc.add_paragraph(
        "• Temporal Dimensions: Extracted purchase year, calendar month, month name, and Year-Month period strings (e.g., '2017-11') "
        "to facilitate time-series aggregation.",
        style='List Bullet'
    )
    doc.add_paragraph(
        "• Customer Frequency & Value Tiers: Computed order count per unique customer and categorized into One-time vs. Repeat, "
        "combined with a median sales value split (BRL 89.81) for segmentation.",
        style='List Bullet'
    )

    # ==========================================
    # 9. EXPLORATORY DATA ANALYSIS
    # ==========================================
    style_heading(doc.add_paragraph(), "9. Exploratory Data Analysis", level=1)
    doc.add_paragraph(
        "Exploratory inspection of global order status revealed that completed transactions ('delivered') represent 97.02% of all "
        "platform records (96,478 out of 99,441 orders). Canceled (0.63%), unavailable (0.61%), and in-transit orders (shipped: 1.11%) "
        "were filtered out to avoid inflating realized commercial revenue."
    )

    # ==========================================
    # 10. BUSINESS QUESTIONS & DETAILED ANALYSES
    # ==========================================
    style_heading(doc.add_paragraph(), "10. Business Questions Overview", level=1)
    doc.add_paragraph(
        "The analytical core is structured around five strategic business questions designed to dissect sales, product, "
        "customer, and regional performance."
    )

    # Section 11: Monthly Sales
    style_heading(doc.add_paragraph(), "11. Business Question 1: Monthly Sales Analysis", level=2)
    doc.add_paragraph(
        "Delivered sales value exhibited pronounced growth across the observed timeline. In 2016, platform records were limited "
        "to early operational testing (yielding BRL 46,653.74). By 2017, volume expanded to BRL 6,921,535.24, and reached BRL 8,451,584.77 "
        "through the active months of 2018."
    )
    doc.add_paragraph(
        "Monthly time-series analysis reveals that November 2017 established the all-time monthly record at BRL 1,153,364.20, "
        "demonstrating the massive commercial impact of Black Friday promotions in the Brazilian market. The lowest observed monthly sales "
        "occurred in December 2016 (BRL 19.62), reflecting an incomplete startup period."
    )

    # Section 12: Product Category
    style_heading(doc.add_paragraph(), "12. Business Question 2: Product Category Performance", level=2)
    doc.add_paragraph(
        "Analysis of delivered sales value across 71 distinct product categories demonstrated strong commercial concentration. "
        "The Top 10 categories account for over 65% of all delivered revenue on the platform:"
    )
    cats_data = [
        ("Health & Beauty", "BRL 1,412,089.53", "9,670", "9.16%"),
        ("Watches & Gifts", "BRL 1,305,541.61", "5,991", "8.47%"),
        ("Bed Bath & Table", "BRL 1,241,681.72", "11,115", "8.05%"),
        ("Sports & Leisure", "BRL 1,156,656.48", "8,641", "7.50%"),
        ("Computers & Accessories", "BRL 1,059,272.40", "7,827", "6.87%"),
        ("Furniture & Decor", "BRL 942,662.89", "8,334", "6.11%"),
        ("Housewares", "BRL 822,578.43", "6,964", "5.34%"),
        ("Cool Stuff", "BRL 719,329.95", "3,796", "4.67%"),
        ("Auto", "BRL 685,384.32", "4,235", "4.45%"),
        ("Garden Tools", "BRL 584,214.11", "4,347", "3.79%")
    ]
    cat_t = doc.add_table(rows=len(cats_data)+1, cols=4)
    cat_t.rows[0].cells[0].paragraphs[0].text = "Category Name"
    cat_t.rows[0].cells[1].paragraphs[0].text = "Delivered Sales (BRL)"
    cat_t.rows[0].cells[2].paragraphs[0].text = "Item Count"
    cat_t.rows[0].cells[3].paragraphs[0].text = "Revenue Share"
    for idx, (cn, rev, cnt, sh) in enumerate(cats_data, start=1):
        cat_t.rows[idx].cells[0].paragraphs[0].text = cn
        cat_t.rows[idx].cells[1].paragraphs[0].text = rev
        cat_t.rows[idx].cells[2].paragraphs[0].text = cnt
        cat_t.rows[idx].cells[3].paragraphs[0].text = sh
    format_table(cat_t)

    # Section 13: Customer Analysis
    style_heading(doc.add_paragraph(), "13. Business Question 3: Customer Purchasing Behavior", level=2)
    doc.add_paragraph(
        "A critical strategic finding concerns customer order frequency. Of the 93,358 unique customers who received completed orders, "
        "90,557 (97.00%) placed exactly one order, while 2,801 (3.00%) were repeat buyers."
    )
    doc.add_paragraph(
        "Crucially, repeat buyers demonstrated an average delivered sales value of BRL 308.53 per customer, nearly double the BRL 160.73 "
        "average observed for one-time buyers. This confirms an empirical association where customer retention correlates with higher overall revenue."
    )

    # Section 14: Geographic Analysis
    style_heading(doc.add_paragraph(), "14. Business Question 4: Geographic Sales Distribution", level=2)
    doc.add_paragraph(
        "Evaluating customer geography across all 27 Brazilian states demonstrates extreme territorial concentration. "
        "The Southeast region accounts for the overwhelming majority of commercial volume:"
    )
    state_data = [
        ("São Paulo (SP)", "BRL 5,769,703.15", "40,494", "37.42%"),
        ("Rio de Janeiro (RJ)", "BRL 2,055,401.57", "12,350", "13.33%"),
        ("Minas Gerais (MG)", "BRL 1,818,891.67", "11,355", "11.80%"),
        ("Rio Grande do Sul (RS)", "BRL 861,472.79", "5,342", "5.59%"),
        ("Paraná (PR)", "BRL 781,708.80", "4,923", "5.07%"),
        ("Santa Catarina (SC)", "BRL 595,127.78", "3,547", "3.86%"),
        ("Bahia (BA)", "BRL 591,137.81", "3,256", "3.83%"),
        ("Distrito Federal (DF)", "BRL 346,123.35", "2,097", "2.24%"),
        ("Goiás (GO)", "BRL 334,212.35", "1,980", "2.17%"),
        ("Espírito Santo (ES)", "BRL 317,657.93", "2,007", "2.06%")
    ]
    st_t = doc.add_table(rows=len(state_data)+1, cols=4)
    st_t.rows[0].cells[0].paragraphs[0].text = "State (Federative Unit)"
    st_t.rows[0].cells[1].paragraphs[0].text = "Delivered Sales (BRL)"
    st_t.rows[0].cells[2].paragraphs[0].text = "Delivered Orders"
    st_t.rows[0].cells[3].paragraphs[0].text = "National Share"
    for idx, (st, rev, ords, sh) in enumerate(state_data, start=1):
        st_t.rows[idx].cells[0].paragraphs[0].text = st
        st_t.rows[idx].cells[1].paragraphs[0].text = rev
        st_t.rows[idx].cells[2].paragraphs[0].text = ords
        st_t.rows[idx].cells[3].paragraphs[0].text = sh
    format_table(st_t)
    doc.add_paragraph(
        "By contrast, northern frontier states like Roraima (RR) recorded the lowest total delivered sales value at BRL 9,039.52. "
        "Methodological note: These disparities reflect demographic density and logistics infrastructure rather than localized marketing underperformance."
    )

    # Section 15: Customer Segmentation
    style_heading(doc.add_paragraph(), "15. Customer Segmentation (4 Behavioral Quadrants)", level=1)
    doc.add_paragraph(
        "To establish actionable marketing cohorts, customers were classified into four segments using order frequency and "
        "a median delivered sales value threshold (BRL 89.81):"
    )
    seg_data = [
        ("High-Value One-time", "44,310", "47.46%", "BRL 11,626,953.48", "75.40%", "BRL 262.40"),
        ("Low-Value One-time", "46,247", "49.54%", "BRL 2,928,632.81", "19.00%", "BRL 63.33"),
        ("High-Value Repeat", "2,467", "2.64%", "BRL 836,632.50", "5.43%", "BRL 339.13"),
        ("Low-Value Repeat", "334", "0.36%", "BRL 27,554.96", "0.18%", "BRL 82.50")
    ]
    seg_t = doc.add_table(rows=len(seg_data)+1, cols=6)
    seg_t.rows[0].cells[0].paragraphs[0].text = "Customer Segment"
    seg_t.rows[0].cells[1].paragraphs[0].text = "Customer Count"
    seg_t.rows[0].cells[2].paragraphs[0].text = "Customer %"
    seg_t.rows[0].cells[3].paragraphs[0].text = "Delivered Revenue (BRL)"
    seg_t.rows[0].cells[4].paragraphs[0].text = "Revenue %"
    seg_t.rows[0].cells[5].paragraphs[0].text = "Avg Revenue (BRL)"
    for idx, (sname, cc, cp, tr, rp, ar) in enumerate(seg_data, start=1):
        seg_t.rows[idx].cells[0].paragraphs[0].text = sname
        seg_t.rows[idx].cells[1].paragraphs[0].text = cc
        seg_t.rows[idx].cells[2].paragraphs[0].text = cp
        seg_t.rows[idx].cells[3].paragraphs[0].text = tr
        seg_t.rows[idx].cells[4].paragraphs[0].text = rp
        seg_t.rows[idx].cells[5].paragraphs[0].text = ar
    format_table(seg_t)

    add_callout(
        doc,
        "High-Value One-time customers represent the largest single revenue engine (75.40% of all delivered sales). "
        "Converting even a modest fraction of this group into repeat purchasers represents the platform's single greatest growth opportunity.",
        title="SEGMENTATION STRATEGIC TAKEAWAY:"
    )

    # Section 16: Customer + Product Affinity
    style_heading(doc.add_paragraph(), "16. Customer + Product Affinity (High-Value Repeat Cohort)", level=2)
    doc.add_paragraph(
        "Mapping line items back to the High-Value Repeat segment identified the specific product categories driving loyal spending:"
    )
    hvr_cats = [
        ("Bed Bath & Table", "BRL 111,503.82", "1,241 items"),
        ("Sports & Leisure", "BRL 80,661.48", "670 items"),
        ("Furniture & Decor", "BRL 77,117.04", "804 items"),
        ("Computers & Accessories", "BRL 68,673.99", "459 items"),
        ("Health & Beauty", "BRL 61,394.83", "551 items")
    ]
    hvr_t = doc.add_table(rows=len(hvr_cats)+1, cols=3)
    hvr_t.rows[0].cells[0].paragraphs[0].text = "Top Category for High-Value Repeat"
    hvr_t.rows[0].cells[1].paragraphs[0].text = "Delivered Sales Value (BRL)"
    hvr_t.rows[0].cells[2].paragraphs[0].text = "Purchased Line Items"
    for idx, (cat, val, itms) in enumerate(hvr_cats, start=1):
        hvr_t.rows[idx].cells[0].paragraphs[0].text = cat
        hvr_t.rows[idx].cells[1].paragraphs[0].text = val
        hvr_t.rows[idx].cells[2].paragraphs[0].text = itms
    format_table(hvr_t)

    # Section 17: Hypothesis Testing
    style_heading(doc.add_paragraph(), "17. Statistical Hypothesis Testing", level=1)
    doc.add_paragraph(
        "To evaluate business assertions with scientific rigor, three formal hypotheses were examined:"
    )
    doc.add_paragraph(
        "• Hypothesis 1 (Inferential Welch's t-test): Evaluated whether repeat customers have a statistically significantly higher "
        "average sales value than one-time customers. Given unequal group sizes (2,801 vs 90,557) and heteroskedasticity, Welch's t-test was employed. "
        "Results: t-statistic = 24.5016, p-value < 0.0001 (numerically approx. 0). Conclusion: Reject H0; repeat customers exhibit a statistically "
        "higher average customer sales value (association confirmed, causality not implied).",
        style='List Bullet'
    )
    doc.add_paragraph(
        "• Hypothesis 2 (Descriptive Revenue Contribution): Compared revenue generated by High-Value vs. Low-Value cohorts. "
        "High-Value customers generated BRL 12,463,585.98 compared to BRL 2,956,187.77 for Low-Value customers (a 4.22x multiple). "
        "Methodological Note: Treated strictly as a descriptive metric since groups were created via median partitioning.",
        style='List Bullet'
    )
    doc.add_paragraph(
        "• Hypothesis 3 (Descriptive Geographic Variance): Evaluated spatial disparity across states, noting a range from BRL 5.77M (SP) "
        "to BRL 9.04K (RR). Categorized as descriptive spatial analysis reflecting demographic and infrastructure variances.",
        style='List Bullet'
    )

    # Section 18: Key Observations
    style_heading(doc.add_paragraph(), "18. Key Observations", level=1)
    obs_list = [
        "November 2017 recorded the highest monthly delivered sales value at BRL 1,153,364.20.",
        "Health & Beauty was the highest-selling product category by delivered sales value at BRL 1,412,089.53.",
        "Repeat customers had a higher average delivered sales value per customer than one-time customers: BRL 308.53 vs BRL 160.73.",
        "São Paulo recorded the highest delivered sales value among Brazilian customer states at BRL 5,769,703.15.",
        "High-value customers generated substantially more delivered sales value than low-value customers: BRL 12,463,585.98 vs BRL 2,956,187.77."
    ]
    for idx, obs in enumerate(obs_list, start=1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r_num = p.add_run(f"Observation {idx}: ")
        r_num.font.bold = True
        p.add_run(obs)

    # Section 19: Business Insights
    style_heading(doc.add_paragraph(), "19. Business Insights", level=1)
    ins_list = [
        "November 2017 showed the strongest monthly delivered sales value, indicating a period of particularly high purchasing activity driven by nationwide Black Friday retail promotions.",
        "Health & Beauty generated the highest delivered sales value among product categories, demonstrating strong underlying consumer demand and high basket value.",
        "Repeat customers had a higher average delivered sales value per customer than one-time customers, demonstrating an association between repeat purchasing and higher customer value.",
        "São Paulo recorded the highest delivered sales value among all states, indicating strong sales activity, mature logistics, and dense consumer adoption in this geographic market.",
        "High-value customers contributed substantially more delivered sales value than low-value customers, highlighting the critical importance of understanding and serving higher-value customer segments."
    ]
    for idx, ins in enumerate(ins_list, start=1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r_num = p.add_run(f"Insight {idx}: ")
        r_num.font.bold = True
        p.add_run(ins)

    # Section 20: Business Recommendations
    style_heading(doc.add_paragraph(), "20. Business Recommendations", level=1)
    doc.add_paragraph(
        "Based directly on the empirical findings, three actionable business recommendations are presented:"
    )
    recs = [
        ("Recommendation 1: Strengthen Customer Retention Programs",
         "Develop personalized retention campaigns targeting High-Value One-time customers (44,310 users). "
         "Deploy automated post-purchase communication sequences 14–30 days after delivery featuring product recommendations "
         "in categories with high repeat affinity (e.g., Bed Bath & Table, Health & Beauty). Target: Increase repeat customer share from 3.0% to 5.0%."),
        ("Recommendation 2: Prioritize High-Performing Categories",
         "Focus merchandising and inventory planning on top revenue generators (Health & Beauty, Watches & Gifts, Bed Bath & Table). "
         "Deepen supplier partnerships, negotiate favorable wholesale pricing, and optimize promotional ad spend during peak Q4 seasonal spikes."),
        ("Recommendation 3: Regional Logistics & Fulfillment Optimization",
         "Align supply chain operations with regional demand concentration by establishing regional fulfillment micro-hubs in the Southeast "
         "(São Paulo, Rio de Janeiro, Minas Gerais). This reduces average shipping times and freight fees, which directly improves customer conversion."
        )
    ]
    for title, desc in recs:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"{title}\n")
        r.font.bold = True
        r.font.color.rgb = RGBColor(26, 54, 93)
        p.add_run(desc)

    # Section 21: AI Integration
    style_heading(doc.add_paragraph(), "21. AI Integration (Google Gemini)", level=1)
    doc.add_paragraph(
        "Artificial Intelligence assistance (Google Gemini) was integrated into the project workflow in Google Colab as an analytical copilot: "
        "(1) Accelerating Python code generation for complex multi-table joins; (2) Recommending statistical frameworks (Welch's t-test); "
        "(3) Structuring visual aesthetics; and (4) Translating raw numerical aggregations into cohesive business narratives."
    )
    doc.add_paragraph(
        "Academic Integrity Affirmation: AI assistance was restricted to collaborative support. All numerical statistics, p-values, "
        "and data structures were computed directly by Python code executing against the empirical Olist dataset."
    )

    # Section 22: Tools and Technologies
    style_heading(doc.add_paragraph(), "22. Tools and Technologies", level=1)
    tech_stack = [
        ("Python 3.10+", "Primary object-oriented data science language"),
        ("Pandas", "Relational data integration, filtering, aggregation, and quality auditing"),
        ("NumPy", "Vectorized numerical transformations and statistical arrays"),
        ("Matplotlib", "Custom visualization design for line and horizontal bar charts"),
        ("SciPy (scipy.stats)", "Inferential statistical hypothesis testing (Welch's t-test)"),
        ("Google Gemini", "AI-assisted analytical co-pilot for code structuring and insights"),
        ("python-docx", "Automated, programmatic academic report compilation")
    ]
    tech_t = doc.add_table(rows=len(tech_stack)+1, cols=2)
    tech_t.rows[0].cells[0].paragraphs[0].text = "Technology / Tool"
    tech_t.rows[0].cells[1].paragraphs[0].text = "Functional Role in Project"
    for idx, (t, r) in enumerate(tech_stack, start=1):
        tech_t.rows[idx].cells[0].paragraphs[0].text = t
        tech_t.rows[idx].cells[1].paragraphs[0].text = r
    format_table(tech_t)

    # Section 23: Limitations
    style_heading(doc.add_paragraph(), "23. Limitations", level=1)
    doc.add_paragraph("Several analytical limitations should be taken into account when interpreting these results:")
    limits = [
        "Temporal Edge Incompleteness: Early 2016 and late 2018 records represent partial operational periods; year-over-year metrics must be interpreted with caution.",
        "Non-Causal Observational Data: Higher average spend among repeat customers reflects an empirical association rather than proof that repeat purchasing causes higher expenditure.",
        "Threshold Sensitivity: Customer segmentation boundaries were defined using a median split; alternative clustering methods (e.g., RFM, K-Means) would produce different segment boundaries.",
        "Absence of External Factors: Macroeconomic indicators (inflation, consumer sentiment, competitor actions) are not captured in the operational logs."
    ]
    for lim in limits:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(2)
        p.add_run(lim)

    # Section 24: Conclusion & References
    style_heading(doc.add_paragraph(), "24. Conclusion & References", level=1)
    doc.add_paragraph(
        "This project successfully designed, implemented, and documented an AI-powered sales intelligence and customer segmentation "
        "system using the Brazilian E-Commerce Public Dataset by Olist. By integrating 110,197 delivered transaction records, the study "
        "identified critical seasonal revenue peaks (November 2017 at BRL 1.15M), quantified category concentration (Health & Beauty at BRL 1.41M), "
        "statistically validated repeat buyer expenditure differentials (Welch's t = 24.5016, p < 0.001), mapped heavy geographic concentration "
        "in São Paulo (37.42% market share), and formulated an actionable retention roadmap."
    )
    doc.add_paragraph("References & Data Sources:\n"
                      "1. Olist E-Commerce Dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce\n"
                      "2. McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference.\n"
                      "3. Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering, 9(3), 90-95.\n"
                      "4. Welch, B. L. (1947). The generalization of 'Student's' problem when several different population variances are involved. Biometrika, 34(1/2), 28-35.")

    out_file = "Anurag_Ranjan_ProjectReport.docx"
    doc.save(out_file)
    print(f"Project report successfully compiled to DOCX at: {os.path.abspath(out_file)}")

if __name__ == "__main__":
    generate_report()
