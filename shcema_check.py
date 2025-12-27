lt = [
    {
  "id": 1001,
  "event_name": "checkout",
  "event_time": "2025-01-15T12:30:45Z",
  "is_success": True,
  "retry_count": 0,
  "latency_ms": 183.75,
  "error_message": '',

  "user": {
    "user_id": 99887766,
    "country": "US",
    "is_premium": False
  },

  "items": [
    {
      "sku": "SKU-101",
      "qty": 1,
      "price": 49.99
    }
  ],

  "tags": ["mobile", "promo"],

  "metrics": {
    "cpu": 0.82,
    "memory_mb": 512
  },

  "attributes": {
    "source": "app",
    "campaign": "new_year"
  }
}
]

# Strict Schema - 
schema = StructType([
    StructField('id',IntegerType(),True),
    StructField('event_name',StringType(),True),
    StructField('event_time',StringType(),True),
    StructField('is_success',BooleanType(),True),
    StructField('retry_count',IntegerType(),True),
    StructField('latency_ms',FloatType(),True),
    StructField('error_message',StringType(),True),
    StructField('user',StructType([
        StructField('user_id',IntegerType(),True),
        StructField('country',StringType(),True),
        StructField('is_premium',BooleanType(),True),
    ]),True),
    StructField('items',ArrayType(StructType([
        StructField('sku',StringType(),True),
        StructField('qty',IntegerType(),True),
        StructField('price',FloatType(),True),
    ]),True),True),
    StructField('tags',ArrayType(StringType(),True),True),
    StructField('metrics',StructType([
        StructField('cpu',FloatType(),True),
        StructField('memory_mb',IntegerType(),True),
    ]),True),
    StructField('attributes',StructType([
        StructField('source',StringType(),True),
        StructField('campaign',StringType(),True),
    ]),True)
])

# Output - 
    # root
    #  |-- id: integer (nullable = true)
    #  |-- event_name: string (nullable = true)
    #  |-- event_time: string (nullable = true)
    #  |-- is_success: boolean (nullable = true)
    #  |-- retry_count: integer (nullable = true)
    #  |-- latency_ms: float (nullable = true)
    #  |-- error_message: string (nullable = true)
    #  |-- user: struct (nullable = true)
    #  |    |-- user_id: integer (nullable = true)
    #  |    |-- country: string (nullable = true)
    #  |    |-- is_premium: boolean (nullable = true)
    #  |-- items: array (nullable = true)
    #  |    |-- element: struct (containsNull = true)
    #  |    |    |-- sku: string (nullable = true)
    #  |    |    |-- qty: integer (nullable = true)
    #  |    |    |-- price: float (nullable = true)
    #  |-- tags: array (nullable = true)
    #  |    |-- element: string (containsNull = true)
    #  |-- metrics: struct (nullable = true)
    #  |    |-- cpu: float (nullable = true)
    #  |    |-- memory_mb: integer (nullable = true)
    #  |-- attributes: struct (nullable = true)
    #  |    |-- source: string (nullable = true)
    #  |    |-- campaign: string (nullable = true)

# System Defined Output- 
    # root
    #  |-- attributes: map (nullable = true)
    #  |    |-- key: string
    #  |    |-- value: string (valueContainsNull = true)
    #  |-- error_message: string (nullable = true)
    #  |-- event_name: string (nullable = true)
    #  |-- event_time: string (nullable = true)
    #  |-- id: long (nullable = true)
    #  |-- is_success: boolean (nullable = true)
    #  |-- items: array (nullable = true)
    #  |    |-- element: map (containsNull = true)
    #  |    |    |-- key: string
    #  |    |    |-- value: string (valueContainsNull = true)
    #  |-- latency_ms: double (nullable = true)
    #  |-- metrics: map (nullable = true)
    #  |    |-- key: string
    #  |    |-- value: double (valueContainsNull = true)
    #  |-- retry_count: long (nullable = true)
    #  |-- tags: array (nullable = true)
    #  |    |-- element: string (containsNull = true)
    #  |-- user: map (nullable = true)
    #  |    |-- key: string
    #  |    |-- value: long (valueContainsNull = true)