  # 🇳🇱 Dutch National Flag Algorithm
  (Three-way partitioning in one pass, constant space)
  

  The Dutch National Flag algorithm is an efficient **in-place partitioning technique** used to sort elements into **three distinct categories** in a single pass.

  It is commonly demonstrated with arrays containing only `0`, `1`, and `2`, but the idea generalizes to real-world classification problems.

  ---

  ## What it really is

  The algorithm partitions an array into three regions:

  - Low region (e.g., all 0s)  
  - Middle region (e.g., all 1s)  
  - High region (e.g., all 2s)  

  It achieves this using **three pointers** and completes in **O(n) time with O(1) space**.

  Think of it as:  
  > Fast categorization into low / medium / high — without extra memory.

  ---

  ## This matters when

  - You need **in-place sorting**
  - You want better than O(n log n) sorting for small category data
  - You’re implementing **3-way partition in QuickSort**
  - Data must be grouped into priorities or flags (low / medium / high)
  - Systems require fast classification logic

  ---

  ## Workflow

  Maintain three pointers:

  - `low`  → boundary of low group  
  - `mid`  → current element  
  - `high` → boundary of high group  

  Process elements while `mid <= high`:

  - If element is in low group → swap with `low`, move both forward  
  - If element is in middle group → move `mid` forward  
  - If element is in high group → swap with `high`, move `high` backward (do not move `mid` yet)

  ---

  ## Example

  ### Input
