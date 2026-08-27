# Day 22 — `*args` and `**kwargs`

📌 **Overview**

Day 22 focuses on variable-length argument handling in Python using `*args` (positional arguments packing) and `**kwargs` (keyword arguments packing).

In Data Science, data engineering, and framework design (like custom estimators in scikit-learn or model pipelines in PyTorch/TensorFlow), functions often need to accept dynamic, arbitrary arguments without changing their base signature.

Mastering `*args` and `**kwargs` allows you to create flexible wrapper functions, decorators, dynamic aggregators, and modular pipelines that seamlessly forward configurations downstream.

---

📚 **Topics Covered**

* Variable-length positional arguments (`*args`)
* Variable-length keyword arguments (`**kwargs`)
* Unpacking operators (`*` for iterables, `**` for dictionaries)
* Standard parameter ordering: `def func(pos, *args, kw_only, **kwargs)`
* Forwarding arguments to downstream functions (Function Wrapping)
* Building flexible mathematical aggregators
* Dynamic model and pipeline configurations

---

