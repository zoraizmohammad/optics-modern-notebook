## 📊 `matplotlib.pyplot.hist` – Overview

This function plots a **histogram**, which is a way to visualize the distribution of a dataset by grouping it into **bins**.

---

## 🧾 **Function Syntax:**

```python
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, cumulative=False, 
                       bottom=None, histtype='bar', align='mid', orientation='vertical', 
                       rwidth=None, log=False, color=None, label=None, stacked=False, 
                       edgecolor=None, linewidth=None, alpha=None, ... )
```

---

## 🔹 **Key Parameters:**

| Parameter         | Description |
|------------------|-------------|
| `x`              | The data to plot (array-like). |
| `bins`           | Number of bins (int) or custom bin edges (list/array). Default: auto. |
| `range`          | Tuple (min, max) for the histogram range. |
| `density`        | If `True`, area under histogram = 1 (shows probability density). |
| `cumulative`     | If `True`, shows cumulative histogram. |
| `bottom`         | Starting point for each bin (e.g., stack histograms). |
| `histtype`       | `'bar'`, `'barstacked'`, `'step'`, `'stepfilled'`. |
| `align`          | `'left'`, `'mid'`, or `'right'` for bar alignment. |
| `orientation`    | `'vertical'` or `'horizontal'`. |
| `rwidth`         | Relative width of bars (e.g., 0.8). |
| `log`            | If `True`, y-axis will be log-scaled. |
| `color`          | Bar color. Can be a string or list of colors. |
| `label`          | Label for the legend. |
| `stacked`        | If `True`, stacks multiple datasets. |
| `edgecolor`      | Color of bar edges. |
| `linewidth`      | Width of bar edges. |
| `alpha`          | Transparency (0 = fully transparent, 1 = solid). |

---

## 🔁 **Returns:**

```python
n, bins, patches = plt.hist(...)
```

| Return     | Description |
|------------|-------------|
| `n`        | Array of bin counts (or densities if `density=True`) |
| `bins`     | Array of bin edges |
| `patches`  | List of `Rectangle` objects (the actual bar graphics) |

---

## ✅ Example:

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

n, bins, patches = plt.hist(data, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7)

plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()
```

---

Let me know if you'd like a visual cheat sheet or want to experiment with different parameter values!
