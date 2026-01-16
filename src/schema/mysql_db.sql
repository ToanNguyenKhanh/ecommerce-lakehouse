USE ecommerce;

CREATE TABLE IF NOT EXISTS customers() {
    customer_id VARCHAR,
    customer_unique_id VARCHAR,
    customer_zip_code_prefix INTEGER,
    customer_city VARCHAR,
    customer_state VARCHAR,
    PRIMARY KEY (customer_id)
}

CREATE TABLE IF NOT EXISTS sellers () {
    seller_id VARCHAR(255),
    seller_zip_code_prefix INTEGER,
    seller_city VARCHAR,
    seller_state VARCHAR,
    PRIMARY KEY (seller_id)
}

CREATE TABLE IF NOT EXISTS geolocation () {
    geolocation_zip_code_prefix INTEGER,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(255)
}

CREATE TABLE IF NOT EXISTS orders() {
    order_id VARCHAR(255),
    customer_id VARCHAR(255),
    order_status VARCHAR(255),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
}

CREATE TABLE IF NOT EXISTS order_items() {
    order_id VARCHAR(255),
    order_item_id INTEGER,
    product_id VARCHAR(255),
    seller_id VARCHAR(255),
    shipping_limit_date TIMESTAMP,
    price DECIMAL
}

CREATE TABLE IF NOT EXISTS order_payments() {
    order_id VARCHAR(255),
    payment_sequential INTEGER,
    payment_type VARCHAR,
    payment_installments INTEGER,
    payment_value DECIMAL
}

CREATE TABLE IF NOT EXISTS order_reviews() {
    review_id VARCHAR(255),
    order_id varchar,
    review_score INTEGER,
    review_comment_title VARCHAR,
    review_comment_message VARCHAR,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
}

CREATE TABLE IF NOT EXISTS products() {
    product_id VARCHAR(255),
    product_category_name VARCHAR(255),
    product_name_length INTEGER,
    product_description_length INTEGER,
    product_photos_qty INTEGER,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT
}

CREATE TABLE IF NOT EXISTS product_category_name_translation() {
    product_category_name VARCHAR(255),
    product_category_name_english VARCHAR(255)
}

CREATE TABLE IF NOT EXISTS marketing_qualified_leads() {
    mql_id VARCHAR(255),
    first_contact_date TIMESTAMP,
    landing_page_id VARCHAR(255),
    origin VARCHAR(255),
}

CREATE TABLE IF NOT EXISTS closed_deals() {
    mql_id VARCHAR(255),
    seller_id VARCHAR(255),
    sdr_id VARCHAR(255),
    sr_id VARCHAR(255),
    business_segment VARCHAR(255),
    lead_type VARCHAR(255),
    lead_behaviour_profile VARCHAR(255),
    has_company VARCHAR(255),
    has_gtin VARCHAR,
    average_stock VARCHAR,
    business_type VARCHAR,
    declared_product_catalog_size INTEGER,
    declared_monthly_revenue FLOAT,
    won_date TIMESTAMP
}