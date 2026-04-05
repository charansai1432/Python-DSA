Here the sliding window has fixed & variable size approach's

SW mainlny works only (+ve elements) in a array 

    -- The SW fails when negative elements are present 



Identifying -- <FOR FIXED SLIDING WINDOW >

        - If a question says fixed window of size K ==> fixed SW technique



<FOR VARIABLE SLIDING WINDOW>

        - If a question does not contain any size use the variable sliding windew 
            - and question mentions something like atmost, exactly , distinct , k flips,k erros,k mismatches, char replacements == . use the variable Variable Sw 

If a question mentions some thing like absoulte diff <= k  (dont assume it is a fixed SW technique)
it is variable Sw technique because Here they didnot mention the window size okk i.e (varaible SW using Deque technique we solve the problem )


<KADANE ALGO >  -- It is a optimization technique that can be used in atmost k elements look similarly like an varaible SW but not 

        - used mainly if a array contain -ve elements
        - question having the maximum,minimum subarray sum if a question contain something like this 
        - this it is kadane algo question 





<Prefix sum>

    - used when the if a array contain the -ve elements
    - If the question is saying the longest subarray sum = k , count subaray sum =k , sum divisble by k
    - If this conditions mention in a question then it is prefix sum question 

    - if a question contain atleast maximum sum subarray then it is (kadane's + prefix logic question )

    
