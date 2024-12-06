# swap strings using len function and string slicing (no new bucket variables allowed)
bucket1 = "oil"
bucket2 = "water"

# use string concatenation to print existing contents
print("bucket 1 is filled with " + bucket1)
print("bucket 2 is filled with " + bucket2)

# save len of bucket1
bucket1_len = len(bucket1)

# concat both strings into the bucket1 (pour the water into the oil)
bucket1 = bucket1 + bucket2

# assign bucket2 the first char (zero-based) until length of bucket1 (skim the oil off the top into now empty bucket)
bucket2 = bucket1[0:bucket1_len]

# assign bucket1 with the residual (only water should remain in the bucket)
bucket1 = bucket1[bucket1_len:]

# use Formatted string literals (f-strings) to print new contents
print(f"\nbucket 1 is now filled with {bucket1}\nbucket 2 is now filled with {bucket2}")
