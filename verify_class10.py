#!/usr/bin/env python3
"""Independent exact dynamic-programming audit of consecutive Class 10.
Python 3.10+, standard library only; no network or third-party packages.
"""
import argparse
import csv
import itertools
import math
from fractions import Fraction
from pathlib import Path

FORBIDDEN = {(1, 2, 3), (1, 3, 2), (3, 1, 2)}
ALLOWED = {(2, 1, 3), (2, 3, 1), (3, 2, 1)}


def pattern(t):
    order = sorted(t)
    return tuple(order.index(x) + 1 for x in t)


def brute(n):
    counts = [[0] * (n + 1) for _ in range(4)]
    for perm in itertools.permutations(range(1, n + 1)):
        pats = [pattern(perm[i:i + 3]) for i in range(n - 2)]
        if any(p in FORBIDDEN for p in pats):
            continue
        counts[0][perm[-1]] += 1
        for j, p in enumerate(((2, 1, 3), (2, 3, 1), (3, 2, 1)), 1):
            counts[j][perm[-1]] += pats.count(p)
    return counts


def compute(max_n):
    data = [None] * (max_n + 1)
    data[1] = [[0, 1], [0, 0], [0, 0], [0, 0]]
    if max_n >= 2:
        data[2] = [[0, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    totals = [0] * (max_n + 1)
    totals[1] = 1
    if max_n >= 2:
        totals[2] = 2
    for n in range(3, max_n + 1):
        m = n - 2
        prev = data[n - 1]
        prev2 = data[m]
        current = [[0] * (n + 1) for _ in range(4)]
        c, q213, q231, q321 = current
        A_nm1, A_nm2 = totals[n-1], totals[m]
        c[1] = A_nm1
        q213[1] = sum(prev[1])
        q231[1] = sum(prev[2]) + A_nm1 - A_nm2
        q321[1] = sum(prev[3]) + A_nm2 if n >= 3 else sum(prev[3])
        partial = [0] * 4
        for k in range(3, n + 1):
            r = k - 2
            for stat in range(4):
                partial[stat] += prev2[stat][r]
            c[k] = partial[0]
            q213[k] = partial[1] + partial[0]
            q231[k] = partial[2] + (partial[0] - prev2[0][1] if m >= 2 else 0)
            q321[k] = partial[3] + (prev2[0][1] if m >= 2 else 0)
        data[n] = current
        totals[n] = sum(c)
        assert sum(q213) + sum(q231) + sum(q321) == (n-2) * totals[n]
    return data, totals


def oeis_a079512(limit):
    """Independent, previously published Kitaev recurrence, OEIS A079512."""
    a = [0] * (limit + 1)
    a[0] = a[1] = 1
    for n in range(2, limit + 1):
        a[n] = sum(math.comb(n-i-1, i) * a[n-2*i-1] for i in range((n-1)//2 + 1)) + (n+1) % 2
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-n', type=int, default=1200)
    ap.add_argument('--brute-n', type=int, default=8)
    ap.add_argument('--csv', default=None)
    args = ap.parse_args()
    assert args.max_n >= max(3, args.brute_n)
    data, A = compute(args.max_n)
    for n in range(1, min(args.brute_n, args.max_n) + 1):
        expected = brute(n)
        assert expected == data[n], (n, expected, data[n])
    print(f'BRUTE_BY_FINAL_VALUE PASS n=1..{min(args.brute_n, args.max_n)} all 4 statistics')
    published = oeis_a079512(min(100, args.max_n))
    assert all(A[n] == published[n] for n in range(1, min(100, args.max_n) + 1))
    print(f'KNOWN_ENUMERATION_A079512 PASS n=1..{min(100, args.max_n)}')
    print(f'MARKED_IDENTITY PASS n=3..{args.max_n}')
    selected = [3,4,5,6,7,8,9,10,11,12,16,20,30,50,100,200,400,600,800,1000,1200]
    rows = []
    for n in selected:
        if n > args.max_n: continue
        p213, p231, p321 = (sum(data[n][i]) for i in (1,2,3))
        frac = Fraction(p321, n * A[n])
        rows.append([n, A[n], p213, p231, p321, format(float(frac), '.15f')])
        print(f'n={n} total={A[n]} 213={p213} 231={p231} 321={p321} normalized_321={float(frac):.12f}')
    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['n','avoiding_permutations','total_213','total_231','total_321','total_321_over_n_times_size'])
            w.writerows(rows)
    print('ALL CHECKS PASS. No asymptotic result is certified.')

if __name__ == '__main__':
    main()
