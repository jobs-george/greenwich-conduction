#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <omp.h>

int main(int argc, char *argv[])
{
    int m, n;
    double tol;

    m = std::atoi(argv[1]);
    n = std::atoi(argv[2]);
    tol = std::atof(argv[3]);

    std::vector<std::vector<double>> t(m + 2, std::vector<double>(n + 2, 30.0));
    std::vector<std::vector<double>> tnew(m + 1, std::vector<double>(n + 1, 0.0));

    double diff, difmax;

    std::cout << m << " " << n << " " << tol << std::endl;

    // Fix boundary conditions
    for (int i = 1; i <= m; i++)
    {
        t[i][0] = 40.0;
        t[i][n + 1] = 90.0;
    }
    for (int j = 1; j <= n; j++)
    {
        t[0][j] = 30.0;
        t[m + 1][j] = 50.0;
    }

    int iter = 0;
    difmax = 1000000.0;
    while (difmax > tol)
    {
        iter++;

// Update temperature for next iteration in parallel
#pragma omp parallel for
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                tnew[i][j] = (t[i - 1][j] + t[i + 1][j] + t[i][j - 1] + t[i][j + 1]) / 4.0;
            }
        }

        // Compute the maximum difference between old and new temperatures
        difmax = 0.0;
#pragma omp parallel for reduction(max : difmax) private(diff)
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                diff = std::fabs(tnew[i][j] - t[i][j]);
                if (diff > difmax)
                {
                    difmax = diff;
                }
                // Copy new to old temperatures
                t[i][j] = tnew[i][j];
            }
        }
    }

    // Print results
    std::cout << "iter = " << iter << "  difmax = " << difmax << std::endl;
    for (int i = 0; i <= m + 1; i++)
    {
        std::cout << std::endl;
        for (int j = 0; j <= n + 1; j++)
        {
            std::cout << t[i][j] << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
