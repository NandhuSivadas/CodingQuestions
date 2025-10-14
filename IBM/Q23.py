

## 🧮 IBM Coding Question — *Minimum Moves for Equal Consignments*

### **Problem Statement**

# You are given an array `quantity`, where `quantity[i]` represents the quantity of the *i-th* item type in a shop’s inventory.
# The shopkeeper wants to divide these items into **two non-empty consignments** `T1` and `T2` such that:

# * `T1` contains items from **index 1 to j**
# * `T2` contains items from **index j+1 to n**
# * Both `T1` and `T2` must be **non-empty**
#   (so `1 ≤ j < n`)

# The **goal** is to make the **total quantities** of both consignments equal using the **minimum number of moves**.

# ---

# ### **Allowed Move**

# In one move, you can:

# * Increase or decrease the quantity of **any item** by `1`.

# > Note: The quantity of any item must always stay **positive**.

# ---

# ### **Objective**

# Find the **minimum total number of moves** required to make the **sum of T1 equal to the sum of T2**, assuming you can choose the **best split point** `j`.

# ---

# ### **Function Description**

# ```python
# def getMinimumMoves(quantity: list[int]) -> int:
#     """
#     quantity: list of integers representing quantities of each item type
#     Returns: integer, the minimum number of moves to make both consignments equal
#     """
# ```

# ---

# ### **Example 1**

# **Input:**

# ```python
# quantity = [1, 4, 4]
# ```

# **Output:**

# ```
# 1
# ```

# **Explanation:**
# Possible splits:

# * Split at `j = 1` →
#   `T1 = [1]`, `T2 = [4, 4]`
#   Sum difference = `|1 - 8| = 7` → 7 moves needed

# * Split at `j = 2` →
#   `T1 = [1, 4]`, `T2 = [4]`
#   Sum difference = `|5 - 4| = 1` → **1 move needed**

# ✅ **Minimum moves = 1**

# ---

# ### **Example 2**

# **Input:**

# ```python
# quantity = [5, 3, 2, 6]
# ```

# **Output:**

# ```
# 0
# ```

# **Explanation:**

# * Split at `j = 2`:
#   `T1 = [5, 3]` → Sum = 8
#   `T2 = [2, 6]` → Sum = 8
#   Both sums already equal → **0 moves needed**

# ✅ **Minimum moves = 0**

# ---

# ### **Constraints**

# * `2 ≤ n ≤ 10^5`
# * `1 ≤ quantity[i] ≤ 10^9`

# ---


def sol(arr):
    total = sum(arr)
    left_sum = 0
    min_diff = float('inf')

    for i in range(len(arr) - 1):
        left_sum += arr[i]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff


