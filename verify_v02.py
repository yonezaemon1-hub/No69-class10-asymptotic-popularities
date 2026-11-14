#!/usr/bin/env python3
"""Author-side finite checks for the No.69 asymptotic proof candidate.

Pure Python 3.10+ standard library. Writes no files and no private logs.
Does NOT prove the infinite-n result or certify historical novelty.
"""
from __future__ import annotations
from itertools import permutations
from math import comb

FORBIDDEN = {(1, 2, 3), (1, 3, 2), (3, 1, 2)}


def pat(triple):
    a, b, c = triple
    return (1 + (b < a) + (c < a),
            1 + (a < b) + (c < b),
            1 + (a < c) + (b < c))


def brute(n):
    count = total_asc = 0
    totals = [0, 0, 0]
    for perm in permutations(range(1, n + 1)):
        patterns = [pat(perm[i:i+3]) for i in range(n - 2)]
        if any(q in FORBIDDEN for q in patterns):
            continue
        count += 1
        K = sum(perm[i] < perm[i+1] for i in range(n-1))
        total_asc += K
        L = int(perm[0] < perm[1])
        R = int(perm[-2] < perm[-1])
        got = [patterns.count(p) for p in ((2,1,3), (2,3,1), (3,2,1))]
        assert got == [K-L, K-R, n-2-2*K+L+R], (perm, got, K, L, R)
        totals = [x+y for x,y in zip(totals,got)]
    return count, total_asc, totals


def endpoint_dp(nmax):
    # Store only the previous two endpoint-refined rows.
    a_prev2, a_prev1 = [0,1], [0,1,1]
    b_prev2, b_prev1 = [0,0], [0,0,1]
    results = {1:(1,0),2:(2,1)}
    for n in range(3,nmax+1):
        a=[0]*(n+1)
        b=[0]*(n+1)
        a[1] = sum(a_prev1)
        b[1] = sum(b_prev1)
        sa=sb=0
        for k in range(3,n+1):
            r=k-2
            sa+=a_prev2[r]
            sb+=b_prev2[r]+a_prev2[r]
            a[k],b[k]=sa,sb
        results[n] = sum(a),sum(b)
        a_prev2,a_prev1 = a_prev1,a
        b_prev2,b_prev1 = b_prev1,b
    return results


def verify_block_lower_bound(nmax=220):
    A=endpoint_dp(nmax)
    for m in (1,2,3,4,5,8):
        s0=8*m
        d=2*m+1
        for n in range(s0,nmax+1):
            B=(n-s0)//d
            bound=1
            for b in range(B):
                s=s0+b*d
                assert comb(s//4,m) >= (s/(8*m))**m * (1-1e-9)
                bound*=comb(s//4,m)
            assert bound <= A[n][0], (n,m,bound,A[n][0])
    print('BLOCK_INJECTION_NUMERICAL_BOUND PASS m=1,2,3,4,5,8; n<=220')


def main():
    A=endpoint_dp(1200)
    for n in range(3,10):
        c,k,counts=brute(n)
        assert (c,k)==A[n], (n,c,k,A[n])
        assert sum(counts)==(n-2)*c
        print(f'INDEPENDENT_BRUTE_AND_ASCENT_DP PASS n={n} A={c} ascents={k} counts={counts}')
    verify_block_lower_bound()
    for n in (50,100,400,800,1200):
        a,k=A[n]
        print(f'ASCENT_EXPECTATION n={n} K_over_n={k/(a*n):.12f} ' \
              f'A_digits={len(str(a))}')
    print('ALL FINITE CHECKS PASS; INFINITE PROOF AND NOVELTY NEED INDEPENDENT AUDIT')

if __name__ == '__main__':
    main()
