\documentclass{article}

\usepackage{geometry}
\usepackage{amsmath}
\usepackage{subfiles}
\usepackage{titleps}
\usepackage{multicol,caption}
\usepackage{enumerate}
\usepackage{listings}
\usepackage[toc,page]{appendix}
\usepackage{graphicx}
\usepackage{wrapfig}
\usepackage{algpseudocode}
\usepackage{algorithm}
\usepackage{xcolor}
\usepackage{pgfplots}
\usepackage{minitoc}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{amsthm}
\pgfplotsset{compat=1.13}
\newenvironment{Figure}
  {\par\medskip\noindent\minipage{\linewidth}}
  {\endminipage\par\medskip}
\lstset{%
  title=\lstname,
  backgroundcolor=\color{white},
  basicstyle=\footnotesize,
  breakatwhitespace=false,
  breaklines=true,
  captionpos=b,
  commentstyle=\color{green},
  extendedchars=true,
  frame=single,
  keepspaces=true,
  keywordstyle=\color{blue},
  language=C++,
  numbers=left,
  numberstyle=\tiny\color{black},
  rulecolor=\color{black},
  showspaces=false,
  showstringspaces=false,
  showtabs=false,
  stepnumber=1,
  stringstyle=\color{magenta},
  tabsize=2
  }

\newtheorem{theorem}

\newpagestyle{doc}{
  \headrule{}
  \footrule{}
  \sethead{\thesection\quad \sectiontitle}{}{\thesubsection\quad
  \subsectiontitle}
  \setfoot{}{\thepage}{}
}
\newpagestyle{toc}{
  \headrule{}
  \footrule{}
  \sethead{CONTENTS}{}{}
  \setfoot{}{\thepage}{}
}
\newpagestyle{abs}{
  \headrule{}
  \footrule{}
  \sethead{ABSTRACT}{}{}
  \setfoot{}{\thepage}{}
}
\pagestyle{doc}

\renewcommand{\thealgorithm}{\arabic{section}.\arabic{subsection}.\Alph{algorithm}}

\title{Algorithm Design}
\author{Arden Rasmussen}
\date{\today}
\linespread{1}
\setcounter{tocdepth}{2}

\begin{document}
\pagenumbering{gobble}
\maketitle
\newpage
\pagestyle{toc}
\tableofcontents
\newpage
\pagestyle{doc}
\pagenumbering{arabic}

\section{Chapter 1}\label{sec:chapter_1}

\subsection{A First Problem Stable Matching}\label{sub:a_first_problem_stable_matching}

\subsubsection{The Question}\label{ssub:the_question}

The Stable Matching Problem originated in 1962 from Davis Gale and Lloyd
Shapley. Gale and Shapley asked: Given a set of preferences among
employers and applicants, can we assign applicants to employers so that
for every employer \(E\), and every applicant \(A\) who is not scheduled
to work for \(E\), at least one of the following two things in the case?

\begin{enumerate}[(i)]
  \item \(E\) prefers everyone of its accepted applicants to \(A\); or
  \item \(A\) prefers her current situation over working for employer \(E\).
\end{enumerate}

If this hold, the outcome is stable: individual self-interest will
prevent any applicant/employer deal from being made behind the scenes.

\paragraph{Formulating the Problem}\label{par:formulating_the_problem}

A ``bare-bones'' version of the problem can be useful for a basic
solution: each of \(n\) applicants applies to each of \(n\) companies,
and each company wants to accept a \emph{single} applicant. This
preserves the fundamental issues of the original problem.

Gale and Shapley, observed that this problem can be viewed as devising a
system that \(n\) men and \(n\) women can end up getting married, and
everyone is seeking to be paired with exactly one individual of the
opposite gender.

So consider a set \(M=\{m_1,\ldots,m_n\}\) of \(n\) men, and a set
\(W=\{w_1,\ldots,w_n\}\) of \(N\) women. Let \(M \times W\) denote the
set of all possible ordered pairs of the form \((m,w)\), where
\(m \in M\) and \(w \in W\), a \emph{matching} \(S\) is a \emph{set} of
ordered pairs, each of \(M \times W\), with the property that each
member of \(M\) and each member of \(W\) appears in at most one pair in
\(S\). A \emph{perfect matching} \(S'\) is a matching with the property
that each member of \(M\) and each member of \(W\) appears in
\emph{exactly} one pair in \(S'\).

Matching and perfect matchings are objects that will recur frequently;
they arise naturally in modeling a wide range of algorithmic problems.

Now we can add the notion of \emph{preferences} to this setting. Each
man \(m \in M\) \emph{ranks} all the women; we will say that
\(m prefers w to w'\) if \(m\) ranks \(w\) higher than \(w'\). We will
refer to the ordered ranking of \(m\) as his preference list. We will
not allow ties in the ranking. Each woman, analogously, ranks all the
men.

Given a perfect matching \(S\), what can go wrong? There is the
situation where: There are two pairs \((m,w)\) and \((m',w')\) in \(S\)
with the property that \(m\) prefers \(w'\) to \(w\), and \(w'\) prefers
\(m\) to \(m'\). In this canse, there's nothing to stop \(m\) and \(w'\)
from abandoning their current partners and heading off together; the set
of marriages is not self enforcing. We'll say that such a pair
\((m, w')\) is an \emph{instability} with respect to \(S\): \((m,w')\)
does not belong to \(S\), but each of \(m\) and \(w'\) prefers the otehr
to their partner in \(S\).

Our goal, then, is a set of marriages with no instabilities. We'll say
that a matching \(S\) is \emph{stable} if

\begin{enumerate}[(i)]
  \item it is perfect, and
  \item there is no instability with respect to \(S\).
\end{enumerate}

Two questions spring immediately to mind:

\begin{itemize}
  \item Does there exist a stable matching for every set of preference lists?
  \item Given a set of preference lists, can we efficiently construct a stable
    match if there is one?
\end{itemize}

It is important to note that it is possible for an instance to have
more than one stable matching.

\subsubsection{Designing the Algorithm}\label{ssub:designing_the_algorithm}

Let us consider some of the basic ideas that motivate the algorithm.

\begin{itemize}
  \item Initially, everyone is unmarried. Suppose an unmarried man \(m\)
    choses the woman \(w\) who ranks highest on his preference list and
    \emph{proposes} to her. Can we declare immediately that \((m,w)\) will
    be one of the pairs in our final stable matching? Not necessarily: at
    some point in the future, a man \(m'\) whom \(w\) prefers may propose
    to her. On the other hand, it would be dangerous for \(w\) to reject
    \(m\) right away; she may never receive a proposal from someone she
    ranks as highly as \(m\). So a natural idea would be to have the pair
    \((m,w)\) enter an intermediate state --- \emph{engagement}.
  \item Suppose we are now at a state in which some men and women are
    \emph{free} --- not engaged --- and some are engaged. The next step
    could look like this. An arbitrary free man \(m\) chooses the
    highest-ranked woman \(w\) to whom he has not yet proposed, and he
    proposes to her. If \(w\) is also free, them \(m\) and \(w\) become
    engaged. Otherwise, \(w\) is already engaged to some other man \(m'\).
    In this case, she determines which of \(m\) or \(m'\) ranks higher on
    her preference list; this man becomes engaged to \(w\) and the other
    becomes free.
  \item Finally, the algorithm will terminate when no one is free; at this
    moment, all engagements are declared final, and the resulting perfect
    matching is returned.
\end{itemize}

\begin{algorithm}[H]
  \caption{Gale-Shapley Algorithm}
  \begin{algorithmic}
    \State{Initially all $m \in M$ and $w \in W$ are free}
    \While{there is a man $m$ who is free and hasn't proposed to every woman}
      \State{Choose such a man $m$}
      \State{Let $w$ be the highest-ranked woman in $m$'s preference list to
      whom $m$ has not yet proposed}
      \If{$w$ is free}
        \State{$(m,w)$ become engaged}
      \Else $w$ is currently engaged to $m'$
        \If{$w$ prefers $m'$ to $m$}
          \State{$m$ remains free}
        \Else $w$ prefers $m$ to $m'$
          \State{$(m,w)$ become engaged}
          \State{$m'$ becomes free}
        \EndIf
      \EndIf
    \EndWhile
    \Return{the set $S$ of engaged pairs}
  \end{algorithmic}
\end{algorithm}

It is intriguing that although this algorithm is quite simple to state, it is
not immediatily obvious that it returns a stable matching, or even a perfect
matching.

\subsubsection{Analyzing the Algorithm}\label{ssub:analyzing_the_algorithm}

First considering the view of a woman $w$ durring the execution of the
algorithm. They are proposed to by a $m$, and she becomes engaged, as time goes
on she may receive additional proposals, accepting those increase the rank of
her partner. We discover the following.

\begin{theorem}
  $w$ remains engaged from the poiint at which she receives her first proposal.
\end{theorem}

\end{document}
