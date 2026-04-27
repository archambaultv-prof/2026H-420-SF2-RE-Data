"""
Comparaison des performances des structures de données
Mesure des temps d'exécution pour insertion, suppression et recherche
"""

import time
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'pile'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'file'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'dictionnaire' / 'equipe_3'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'liste_chainee' / 'BigYahoo'))

# Import custom implementations
try:
    from implementation import Pile as PileCustom
except ImportError:
    PileCustom = None

try:
    from implementation import File as FileCustom
except ImportError as e:
    FileCustom = None

try:
    from implementation import Dictionnaire as DictCustom
except ImportError:
    DictCustom = None

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "liste_chainee",
        Path(__file__).parent.parent.parent / 'liste_chainee' / 'BigYahoo' / 'Implémentation .py'
    )
    liste_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(liste_module)
    ListeChaineeCustom = liste_module.ListeChainee
except Exception as e:
    ListeChaineeCustom = None


# ======================= MEASUREMENT FUNCTIONS =======================

def measure_time(func, *args, **kwargs):
    """Measure execution time of a function"""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) * 1000  # Convert to milliseconds


def test_list_insertion_beginning(n):
    """Test list insertion at beginning"""
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst


def test_list_insertion_end(n):
    """Test list insertion at end"""
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


def test_deque_insertion_beginning(n):
    """Test deque insertion at beginning"""
    dq = deque()
    for i in range(n):
        dq.appendleft(i)
    return dq


def test_deque_insertion_end(n):
    """Test deque insertion at end"""
    dq = deque()
    for i in range(n):
        dq.append(i)
    return dq


def test_dict_insertion(n):
    """Test dictionary insertion"""
    d = {}
    for i in range(n):
        d[i] = i
    return d


def test_dict_lookup(d, n):
    """Test dictionary lookup"""
    for i in range(min(1000, n)):
        _ = d.get(i)


def test_list_lookup(lst, n):
    """Test list lookup"""
    for i in range(min(1000, n)):
        _ = i in lst


def test_list_deletion(n):
    """Test list deletion"""
    lst = list(range(n))
    for i in range(min(1000, n)):
        lst.pop(0)
    return lst


def test_deque_deletion(n):
    """Test deque deletion"""
    dq = deque(range(n))
    for i in range(min(1000, n)):
        dq.popleft()
    return dq


def test_pile_insertion(n):
    """Test custom Pile insertion"""
    if PileCustom is None:
        return None
    pile = PileCustom()
    for i in range(n):
        pile.push(i)
    return pile


def test_dict_custom_insertion(n):
    """Test custom Dictionary insertion"""
    if DictCustom is None:
        return None
    dico = DictCustom()
    for i in range(n):
        dico.ajouter_element(i, i)
    return dico


# ======================= MAIN BENCHMARK =======================

def run_benchmarks():
    """Run all benchmark tests"""
    
    # Test sizes with adaptive limits
    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
    
    results = {
        'list_insert_end': {'sizes': [], 'times': []},
        'list_insert_beginning': {'sizes': [], 'times': []},
        'deque_insert_end': {'sizes': [], 'times': []},
        'deque_insert_beginning': {'sizes': [], 'times': []},
        'list_lookup': {'sizes': [], 'times': []},
        'deque_lookup': {'sizes': [], 'times': []},
        'dict_lookup': {'sizes': [], 'times': []},
        'list_deletion': {'sizes': [], 'times': []},
        'deque_deletion': {'sizes': [], 'times': []},
        'dict_insertion': {'sizes': [], 'times': []},
        'dict_custom_insertion': {'sizes': [], 'times': []},
        'pile_insertion': {'sizes': [], 'times': []},
    }
    
    print("=" * 70)
    print("BENCHMARK: Data Structure Performance Comparison")
    print("=" * 70)
    
    # Benchmark LIST operations
    print("\n[LIST] Insertion at end...")
    for size in sizes:
        if size > 100000:
            # Skip if too slow
            continue
        t = measure_time(test_list_insertion_end, size)
        results['list_insert_end']['sizes'].append(size)
        results['list_insert_end']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    print("\n[LIST] Insertion at beginning...")
    for size in sizes:
        if size > 10000:  # This is O(n²) so keep smaller
            continue
        t = measure_time(test_list_insertion_beginning, size)
        results['list_insert_beginning']['sizes'].append(size)
        results['list_insert_beginning']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    # Benchmark DEQUE operations
    print("\n[DEQUE] Insertion at end...")
    for size in sizes:
        t = measure_time(test_deque_insertion_end, size)
        results['deque_insert_end']['sizes'].append(size)
        results['deque_insert_end']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    print("\n[DEQUE] Insertion at beginning...")
    for size in sizes:
        t = measure_time(test_deque_insertion_beginning, size)
        results['deque_insert_beginning']['sizes'].append(size)
        results['deque_insert_beginning']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    # Benchmark LOOKUP operations
    print("\n[LOOKUP] List lookup...")
    for size in sizes:
        lst = list(range(size))
        t = measure_time(test_list_lookup, lst, size)
        results['list_lookup']['sizes'].append(size)
        results['list_lookup']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
    
    print("\n[LOOKUP] Deque lookup...")
    for size in sizes:
        dq = deque(range(size))
        t = measure_time(lambda d, n: [i in d for i in range(min(1000, n))], dq, size)
        results['deque_lookup']['sizes'].append(size)
        results['deque_lookup']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
    
    print("\n[LOOKUP] Dictionary lookup...")
    for size in sizes:
        d = dict((i, i) for i in range(size))
        t = measure_time(test_dict_lookup, d, size)
        results['dict_lookup']['sizes'].append(size)
        results['dict_lookup']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
    
    # Benchmark DELETION
    print("\n[DELETION] List deletion (pop from beginning)...")
    for size in sizes:
        if size > 10000:
            continue
        t = measure_time(test_list_deletion, size)
        results['list_deletion']['sizes'].append(size)
        results['list_deletion']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    print("\n[DELETION] Deque deletion (pop from beginning)...")
    for size in sizes:
        t = measure_time(test_deque_deletion, size)
        results['deque_deletion']['sizes'].append(size)
        results['deque_deletion']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
        if t > 3000:
            break
    
    # Benchmark DICTIONARY insertion
    print("\n[DICT] Dictionary insertion...")
    for size in sizes:
        t = measure_time(test_dict_insertion, size)
        results['dict_insertion']['sizes'].append(size)
        results['dict_insertion']['times'].append(t)
        print(f"  n={size:7d}: {t:10.3f} ms")
    
    # Benchmark CUSTOM implementations if available
    if DictCustom is not None:
        print("\n[CUSTOM] Dictionary (custom) insertion...")
        for size in sizes:
            if size > 100000:
                continue
            t = measure_time(test_dict_custom_insertion, size)
            results['dict_custom_insertion']['sizes'].append(size)
            results['dict_custom_insertion']['times'].append(t)
            print(f"  n={size:7d}: {t:10.3f} ms")
            if t > 3000:
                break
    
    if PileCustom is not None:
        print("\n[CUSTOM] Pile insertion...")
        for size in sizes:
            t = measure_time(test_pile_insertion, size)
            results['pile_insertion']['sizes'].append(size)
            results['pile_insertion']['times'].append(t)
            print(f"  n={size:7d}: {t:10.3f} ms")
    
    return results


# ======================= PLOTTING FUNCTIONS =======================

def create_graphs(results):
    """Create and save matplotlib graphs"""
    
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Graph 1: Insertion at end (List vs Deque)
    fig, ax = plt.subplots(figsize=(10, 6))
    if results['list_insert_end']['sizes']:
        ax.plot(results['list_insert_end']['sizes'], 
                results['list_insert_end']['times'], 
                'o-', linewidth=2, markersize=8, label='List (append)')
    if results['deque_insert_end']['sizes']:
        ax.plot(results['deque_insert_end']['sizes'], 
                results['deque_insert_end']['times'], 
                's-', linewidth=2, markersize=8, label='Deque (append)')
    ax.set_xlabel('Size (n)', fontsize=12)
    ax.set_ylabel('Time (ms)', fontsize=12)
    ax.set_title('Insertion at End: List vs Deque', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('insertion_end.png', dpi=150)
    print("\n✓ Saved: insertion_end.png")
    plt.close()
    
    # Graph 2: Insertion at beginning (List vs Deque)
    fig, ax = plt.subplots(figsize=(10, 6))
    if results['list_insert_beginning']['sizes']:
        ax.plot(results['list_insert_beginning']['sizes'], 
                results['list_insert_beginning']['times'], 
                'o-', linewidth=2, markersize=8, label='List (insert at 0)')
    if results['deque_insert_beginning']['sizes']:
        ax.plot(results['deque_insert_beginning']['sizes'], 
                results['deque_insert_beginning']['times'], 
                's-', linewidth=2, markersize=8, label='Deque (appendleft)')
    ax.set_xlabel('Size (n)', fontsize=12)
    ax.set_ylabel('Time (ms)', fontsize=12)
    ax.set_title('Insertion at Beginning: List vs Deque', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('insertion_beginning.png', dpi=150)
    print("✓ Saved: insertion_beginning.png")
    plt.close()
    
    # Graph 3: Lookup comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    if results['list_lookup']['sizes']:
        ax.plot(results['list_lookup']['sizes'], 
                results['list_lookup']['times'], 
                'o-', linewidth=2, markersize=8, label='List (in operator)')
    if results['deque_lookup']['sizes']:
        ax.plot(results['deque_lookup']['sizes'], 
                results['deque_lookup']['times'], 
                's-', linewidth=2, markersize=8, label='Deque (in operator)')
    if results['dict_lookup']['sizes']:
        ax.plot(results['dict_lookup']['sizes'], 
                results['dict_lookup']['times'], 
                '^-', linewidth=2, markersize=8, label='Dictionary (get)')
    ax.set_xlabel('Size (n)', fontsize=12)
    ax.set_ylabel('Time (ms)', fontsize=12)
    ax.set_title('Search/Lookup Performance', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('lookup.png', dpi=150)
    print("✓ Saved: lookup.png")
    plt.close()
    
    # Graph 4: Deletion
    fig, ax = plt.subplots(figsize=(10, 6))
    if results['list_deletion']['sizes']:
        ax.plot(results['list_deletion']['sizes'], 
                results['list_deletion']['times'], 
                'o-', linewidth=2, markersize=8, label='List (pop(0))')
    if results['deque_deletion']['sizes']:
        ax.plot(results['deque_deletion']['sizes'], 
                results['deque_deletion']['times'], 
                's-', linewidth=2, markersize=8, label='Deque (popleft)')
    ax.set_xlabel('Size (n)', fontsize=12)
    ax.set_ylabel('Time (ms)', fontsize=12)
    ax.set_title('Deletion from Beginning', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('deletion.png', dpi=150)
    print("✓ Saved: deletion.png")
    plt.close()
    
    # Graph 5: Dictionary insertion
    fig, ax = plt.subplots(figsize=(10, 6))
    if results['dict_insertion']['sizes']:
        ax.plot(results['dict_insertion']['sizes'], 
                results['dict_insertion']['times'], 
                'o-', linewidth=2, markersize=8, label='Dictionary (built-in)')
    if results['dict_custom_insertion']['sizes']:
        ax.plot(results['dict_custom_insertion']['sizes'], 
                results['dict_custom_insertion']['times'], 
                's-', linewidth=2, markersize=8, label='Dictionary (custom)')
    ax.set_xlabel('Size (n)', fontsize=12)
    ax.set_ylabel('Time (ms)', fontsize=12)
    ax.set_title('Dictionary Insertion Performance', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('dict_insertion.png', dpi=150)
    print("✓ Saved: dict_insertion.png")
    plt.close()
    
    # Graph 6: Custom Pile
    if results['pile_insertion']['sizes']:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(results['pile_insertion']['sizes'], 
                results['pile_insertion']['times'], 
                'o-', linewidth=2, markersize=8, label='Pile (custom)')
        ax.set_xlabel('Size (n)', fontsize=12)
        ax.set_ylabel('Time (ms)', fontsize=12)
        ax.set_title('Pile (Custom Stack) Insertion', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xscale('log')
        ax.set_yscale('log')
        plt.tight_layout()
        plt.savefig('pile_insertion.png', dpi=150)
        print("✓ Saved: pile_insertion.png")
        plt.close()


# ======================= ENTRY POINT =======================

if __name__ == '__main__':
    print("\nStarting data structure comparison benchmark...\n")
    
    # Run benchmarks
    results = run_benchmarks()
    
    # Create graphs
    print("\n" + "=" * 70)
    print("Creating graphs...")
    print("=" * 70)
    create_graphs(results)
    
    print("\n" + "=" * 70)
    print("Benchmark completed!")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - insertion_end.png")
    print("  - insertion_beginning.png")
    print("  - lookup.png")
    print("  - deletion.png")
    print("  - dict_insertion.png")
    if results['pile_insertion']['sizes']:
        print("  - pile_insertion.png")
    print("\nOpen README.md for detailed analysis.")
