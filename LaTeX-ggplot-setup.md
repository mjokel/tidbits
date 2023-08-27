# LaTeX ggplot2 Setup

> 28. Feb 2023


## file.tex

Use the following commands to learn about the LaTeX file's `\textwidth` and `\textheight` in mm so that we can configure the plot dimensions accordingly.

````latex
\documentclass[a4paper,10pt]{article}

% determine \textwidth in mm 
%  ~> https://tex.stackexchange.com/a/39385
\usepackage{layouts} 

\begin{document}

textwidth: \printinunitsof{mm}\prntlen{\textwidth}
% 146.99762mm ~> 147mm

textheight: \printinunitsof{mm}\prntlen{\textheight}
% 207.89665mm ~> 207mm

\end{document}
````

## file.r

Note that the `dpi` in `ggsave()` may not really matter, as we are working with vector graphics.

````R
# https://ggplot2.tidyverse.org/articles/faq-customising.html
# 
# ggplot base font size, set in *_theme()
.plot_base_size <- 9


# https://ggplot2-book.org/annotations.html#text-labels
# 
# ggplot `annotate(geom="text", ...)` base font size in mm
.plot_annotation_base_size <- 9 * (25.4 / 72.27)  # convert pt to mm

# ------------------------------------------------------------------


# update plot base font size; default is 11pt
...
theme_classic(base_size = .plot_base_size) +
...

# update geom annotation text size
...
annotate("text", label = "Lorem", vjust = 2, hjust = 1.25, size = .plot_annotation_base_size) +
...

# ------------------------------------------------------------------


# anticipate \textwidth for plot output dimension
ggsave(width = 147, height = 100, unit = "mm")
````
