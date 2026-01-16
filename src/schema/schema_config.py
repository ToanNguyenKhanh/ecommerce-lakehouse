from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoulbeType, DecimalType,TimestampType

def get_schema():
    schema_config = {
        "customers" : StructType([
            StructField("cutomer_id", StringType(), True),
            StructField("customer_unique_id", StringType(), True),
            StructField("customer_zip_code_prefix", IntegerType(), True),
            StructField("customer_city", StringType(), True),
            StructField("customer_state", StringType(), True)
        ]),
        "sellers" : StructType([
            StructField("seller_id", StringType(), True),
            StructField("seller_zip_code_prefix", IntegerType(), True),
            StructField("seller_city", StringType(), True),
            StructField("seller_state", StringType(), True),
        ]),
        "geolocation" : StructType([
            StructField("geolocation_zip_code_prefix", IntegerType(), True),
            StructField("geolocation_lat", DoulbeType(), True),
            StructField("geolocation_lng", DoulbeType(), True),
            StructField("geolocation_city", StringType(), True),
            StructField("geolocation_state", StringType(), True),
        ]),
        "orders" : StructType([
            StructField("order_id", StringType(), True),
            StructField("customer_id", StringType(), True),
            StructField("order_status", StringType(), True),
            StructField("order_purchase_timestamp", TimestampType(), True),
            StructField("order_approved_at", TimestampType(), True),
            StructField("order_delivered_carrier_date", TimestampType(), True),
            StructField("order_delivered_customer_date", TimestampType(), True),
            StructField("order_estimated_delivery_date", TimestampType(), True),
        ]),
        "order_items" : StructType([
            StructType("order_id", StringType(), True),
            StructField("order_item_id", IntegerType(), True),
            StructField("product_id", StringType(), True),
            StructField("seller_id", StringType(), True),
            StructField("shipping_limit_date", StringType(), True),
            StructField("price", DecimalType(), True)
        ]),
        "order_payments" : StructType([
            StructField("order_id", StringType(), True),
            StructField("payment_sequential", IntegerType(), True),
            StructField("payment_type", StringType(), True),
            StructField("payment_installments", IntegerType(), True),
            StructField("payment_value", DecimalType(10, 2), True)
        ]),
        "order_reviews" : StructType([
            StructField("review_id", StringType(), True),
            StructField("order_id", StringType(), True),
            StructField("review_score", IntegerType(), True),
            StructField("review_comment_title", StringType(), True),
            StructField("review_comment_message", StringType(), True),
            StructField("review_creation_date", TimestampType(), True),
            StructField("review_answer_timestamp", TimestampType(), True)
        ]),
        "products" : StructType([
            StructField("product_id", StringType(), True),
            StructField("product_category_name", StringType(), True),
            StructField("product_name_length", IntegerType(), True),
            StructField("product_description_length", IntegerType(), True),
            StructField("product_photos_qty", IntegerType(), True),
            StructField("product_weight_g", DecimalType(), True),
            StructField("product_length_cm", DecimalType(), True),
            StructField("product_height_cm", DecimalType(), True),
            StructField("product_width_cm", DecimalType(), True)
        ]),
        "product_category_name_translation" : StructType([
            StructField("product_category_name", StringType(), True),
            StructField("product_category_name_english", StringType(), True),
        ]),
        "marketing_qualified_leads" : StructType([
            StructField()
        ])
    }