def MyTransform (glueContext, dfc) -> DynamicFrameCollection:
        
    # Importing Functions
    from pyspark.sql.functions import col
    
    # Get the input DynamicFrame
    dyf = dfc.select(list(dfc.keys())[0])
    
    # Convert to DataFrame
    df = dyf.toDF()
    
    # Multiply two columns
    df = df.withColumn(
        "total_value",
        col("Price") * col("Quantity")
    )
    
    # Convert back to DynamicFrame
    result_dyf = DynamicFrame.fromDF(df, glueContext, "result_dyf")
    
    return DynamicFrameCollection({"result": result_dyf}, glueContext)