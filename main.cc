#include <iostream>
#include <thread>
#include <vector>
#include "cards.h"
#include "algorithm"


void explore(long long start, long long end)
{
    std::cout << "Exploring " << start << " to " << end << std::endl;
    for (long long i = start; i < end; i++)
    {
        std::string test = sub_lehmer((long long)(i/168168000));
        if (!(i % 1000000000))
        {
            std::cout << test << std::endl;
            std::cout << "Progress" << i - start << " " <<  " "  <<  end - start<< std::endl;
        }
    }
    std::cout << "Explored " << start << " to " << end << std::endl;
}


int main(void)
{
    // minus a couple threads?
    const unsigned int num_threads = std::thread::hardware_concurrency();
    std::cout << "Using " << num_threads << " threads" << std::endl;
    // could be 6 choose 1 * 6 choose 1 etc
    // 18 choose 3 * 15 choose 3 etc
    const long long total_posibilities = 137225088000;
    const long long partition_size = ((long long) total_posibilities / num_threads) + 1;
    std::vector<std::thread> threads(num_threads);


    sub_lehmer(0);

    for (long long i = 0; i * partition_size < total_posibilities; i++)
    {
        const long long explore_end = std::min((i + 1) * partition_size, total_posibilities);
        threads[i] = std::thread(explore, i*partition_size, explore_end);
    }
    for (auto& th : threads)
    {
        th.join();
    }
    return 0;
}

