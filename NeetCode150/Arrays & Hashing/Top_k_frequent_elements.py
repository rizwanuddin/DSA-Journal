"""
Top K Frequent Elements - Explanation

Given an integer array nums and an integer k, return the k most frequent 
elements within the array.The test cases are generated such that the answer 
is always unique. You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]




# TOP K FREQUENT ELEMENTS — INTERVIEW EXPLANATION

## 1. CLARIFY

"Let me make sure I understand the problem. I'm given an array nums
and an integer k, and I need to return the k most frequently
occurring elements. The answer is guaranteed to be unique, and order
of the output doesn't matter."

## 2. BRUTE FORCE

"The brute-force way is to count the frequency of every element, then
sort all of them by frequency, and take the top k. Sorting the whole
thing costs O(n log n)."

## 3. OPTIMIZE

"Sorting everything works fine here since n isn't huge, so I'll go
with that as my main approach. A further optimization exists using a
heap of size k, which would bring it down to O(n log k), but the
sorting approach is simpler to explain and implement correctly under
interview pressure."

## 4. KEY OBSERVATION

"I don't need to sort by the actual numbers — I need to sort by how
often each number appears. So once I have a frequency count, I need a
way to sort based on that count specifically, not the number itself."

## 5. APPROACH

"First, I'll build a frequency dictionary using Counter, mapping each
number to how many times it appears.

Then I'll sort the dictionary's items by frequency, in descending
order, so the most frequent numbers come first.

I'll take the first k pairs from that sorted list.

Finally, I'll extract just the numbers from those pairs, since the
answer only needs the values, not their counts."

## 6. WHILE CODING

"First, I count how often each number appears using Counter."

freq = Counter(nums)

"Now I sort the frequency pairs by count, descending, so the most
frequent numbers come first."

sorted_pairs = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)

"I take the top k pairs from that sorted list."

top_k = sorted_pairs[:k]

"Finally, I extract just the numbers, dropping the counts, since
that's what the problem expects back."

return [pair[0] for pair in top_k]

## 7. EDGE CASES

"If k equals the total number of unique elements, I just return all
of them, since the slice naturally handles that.

If all elements have the same frequency, any k of them work, since
the problem guarantees a unique valid answer regardless of tie order."

## 8. COMPLEXITY

"Time complexity is O(n log n), dominated by the sort, since counting
frequencies is O(n) but sorting the pairs takes O(n log n).

Space complexity is O(n), since the frequency dictionary can hold up
to n unique elements in the worst case."
"""
class Solution:
    def top_k(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_pairs = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in sorted_pairs[:k]]
        #can replace the last two lines with:
        #sorted_nums = sorted(freq, key=freq.get, reverse=True)
        #return sorted_nums[:k]
"""
sorted_pairs[:k] — a list of the top k tuples, still in (number, count) 
form. Example: if sorted_pairs = [(3, 3), (2, 2), (1, 1)] and k = 2, this 
returns [(3, 3), (2, 2)] — still pairs, counts included.

[pair[0] for pair in sorted_pairs[:k]] — a list comprehension: loop through 
each pair in that sliced list, and keep only pair[0] (the number, dropping 
the count). Using the same example: [(3, 3), (2, 2)] → [3, 2] — just the 
numbers now, which is the actual final answer returned by the function.

about lambda part--
What sorted() needs to know: when you give it a list of items to sort, it 
needs to know what to compare. For simple things like numbers or strings, 
it's obvious — just compare them directly. But for something like a (number
, frequency) pair, there's ambiguity: sort by the number? By the frequency?
 sorted() can't guess, so you have to tell it.

That's literally all key= does — it's a rule you hand sorted() saying "for 
each item, here's what to actually compare." And lambda is just Python's 
way of writing a tiny, throwaway function inline, without giving it a full 
def and a name.

Breaking down lambda pair: pair[1]:

lambda — "I'm about to define a quick function"
pair — the input to that function (one item from the list you're sorting — 
here, a (number, frequency) tuple)
: — separates input from what it returns
pair[1] — the output: index 1 of the tuple, which is the frequency
"""