%%
%% 
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}
\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\ProvidesClass{TCLsem}
              [2001/10/18 v1.1f
              TCL Semester]
\newif\ifgerman  \germanfalse
\newif\ifenglish  \englishfalse
\newif\ifdip  \dipfalse
\newcommand*{\semester}[1]{\def\semesterstring{#1}}
\newcommand*{\assistant}[1]{\def\assistantstring{#1}}
\newcommand*{\vice}[1]{\def\vicestring{#1}}
\newcommand*{\handout}[1]{\def\handoutstring{#1}}
\newcommand*{\handin}[1]{\def\handinstring{#1}}
\newcommand*{\forprefix}[1]{\def\forprefixstring{#1}}
\newcommand*{\assistantprefix}[1]{\def\assistantprefixstring{#1}}
\newcommand*{\viceprefix}[1]{\def\viceprefixstring{#1}}
\newcommand*{\handoutprefix}[1]{\def\handoutprefixstring{#1}}
\newcommand*{\handinprefix}[1]{\def\handinprefixstring{#1}}
\newcommand*{\dateprefix}[1]{\def\dateprefixstring{#1}}
\newcommand*{\departmentgerman}[1]{\def\departmentgermanstring{#1}}
\newcommand*{\departmentenglish}[1]{\def\departmentenglishstring{#1}}
\semester{}
\assistant{}
\vice{}
\handout{}
\handin{}
\forprefix{}
\assistantprefix{}
\viceprefix{}
\handoutprefix{}
\handinprefix{}
\dateprefix{}
\departmentgerman{}
{\departmentenglish{}
\DeclareOption{german}{%
  \forprefix{f\"ur}
  \assistantprefix{Betreuer}
  \viceprefix{Stellvertreter}
  \handoutprefix{Ausgabe}
  \handinprefix{Abgabe}
  \dateprefix{Z\"urich, den}
  \germantrue}
\DeclareOption{english}{%
  \forprefix{for}
  \assistantprefix{Advisor}
  \viceprefix{Co-Advisor}
  \handoutprefix{Handout}
  \handinprefix{Due}
  \dateprefix{Lausanne,}
  \englishtrue\germanfalse}
\DeclareOption{dip}{%
  \diptrue}
\DeclareOption{sem}{%
  \dipfalse}
\DeclareOption{elek}{%
    \departmentgerman{\\[1mm] Electrical Engineering}
    \departmentenglish{\\[1mm]Electrical Engineering}}
\DeclareOption{inf}{%
    \departmentgerman{Informatik}
    \departmentenglish{Computer Science}}
\DeclareOption{phys}{%
    \departmentgerman{Physik}
    \departmentenglish{Physics}}
\DeclareOption{math}{%
    \departmentgerman{Mathematik}
    \departmentenglish{Mathematics}}
\ExecuteOptions{german,sem,elek}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[titlepage,a4paper]{article}
\ifenglish
  \RequirePackage[english]{babel}
\fi
\ifgerman
  \RequirePackage[german]{babel}
  \nonfrenchspacing
\fi
\RequirePackage{a4tcl}
\RequirePackage{EPFLheader}
\RequirePackage{bookman}
\renewcommand{\and}{\\[0.25em]}
\let\students\author
\renewcommand\maketitle{\begin{titlepage}%
    \let\footnotesize\small
    \let\footnoterule\relax
    \let \footnote \thanks
    \null
    \vspace{4.5em}%
    \begin{center}%
      \ifgerman%
        \ifdip
        {\Large\bfseries Diplomarbeit im Studiengang
         \departmentgermanstring\\[4mm]%
         \semesterstring \par}%
        \else
       {\Large\bfseries Semesterarbeit im Studiengang
        \departmentgermanstring\\[4mm]%
        \semesterstring \par}%
        \fi%
      \fi%
      \ifenglish%
        \ifdip
      {\Large\bfseries Master Thesis at the Dept.\ of
       \departmentenglishstring\\[4mm] \semesterstring \par}%
        \else
      {\Large\bfseries Student Project at the Dept.\ of
       \departmentenglishstring\\[4mm] \semesterstring\par}%
        \fi%
      \fi%
      \vspace{1.5em}%
      {\bfseries\forprefixstring\par}%
      \vspace{1.5em}%
      {\Large\bfseries \@author \par}%
      \vfill
      {\Huge\bfseries \@title \par}%
      \vfill
      \begin{tabbing}
        \assistantprefixstring : \hspace{10mm} \= \assistantstring\\
        \viceprefixstring : \> \vicestring\\
        \vspace{2em}\\
        \handoutprefixstring : \> \handoutstring\\
        \handinprefixstring : \> \handinstring\\
      \end{tabbing}
      \vspace{2em}%
    \end{center}%
    \enlargethispage{3\baselineskip}
     \ifenglish
Two copies of the written report are to be turned in. Both copies remain
the property of the Telecommunications Circuits Laboratory.
    \fi
    \par%
    \@thanks
    \null
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
  \global\let\semester\relax
  \global\let\assistant\relax
  \global\let\vice\relax
  \global\let\handout\relax
  \global\let\handin\relax
  \global\let\forprefix\relax
  \global\let\assistantprefix\relax
  \global\let\viceprefix\relax
  \global\let\handoutprefix\relax
  \global\let\handinprefix\relax
  \global\let\semesterstring\@empty
  \global\let\assistantstring\@empty
  \global\let\vicestring\@empty
  \global\let\handoutstring\@empty
  \global\let\handinstring\@empty
  \global\let\forprefixstring\@empty
  \global\let\assistantprefixstring\@empty
  \global\let\viceprefixstring\@empty
  \global\let\handoutprefixstring\@empty
  \global\let\handinprefixstring\@empty
}
\newcommand{\prof}[2][]{%
  \def\@intdate{#1}
  \vfill%
  \ifx\@empty\@intdate
    \dateprefixstring\space \today \hfill Prof.\ Dr.\ #2\hspace{2cm}\\[1.5em]
    \ifenglish%
      \textbf{The thesis will not be accepted without returning of the keys!}
    \else%
      \textbf{Die Arbeit wird ohne R\"uckgabe der Schl\"ussel nicht
       entgegengenommen!}
    \fi
  \else
    \dateprefixstring\space \@intdate \hfill Prof.\ Dr.\ #2\hspace{2cm}\\[1.5em]
    \ifenglish%
      \textbf{The thesis will not be accepted without returning of the keys!}
    \else%
      \textbf{Die Arbeit wird ohne R\"uckgabe der Schl\"ussel nicht
       entgegengenommen!}
    \fi
  \fi
  \vspace{2em}
  \newpage%
  \global\let\@intdate\@empty
  \global\let\dateprefix\relax
  \global\let\dateprefixstring\@empty}
\newcommand{\aprof}[2][]{%
  \def\@intdate{#1}
  \vfill%
  \ifx\@empty\@intdate
    \dateprefixstring\space \today \hfill Prof.\ Dr.\ #2\hspace{2cm}\\[1.5em]
    \ifenglish%
      \textbf{The thesis will not be accepted without returning of the keys!}
    \else%
      \textbf{Die Arbeit wird ohne R\"uckgabe der Schl\"ussel nicht
       entgegengenommen!}
    \fi
  \else
    \dateprefixstring\space \@intdate \hfill Prof.\ Dr.\ #2\hspace{2cm}\\[1.5em]
    \ifenglish%
      \textbf{The thesis will not be accepted without returning of the keys!}
    \else%
      \textbf{Die Arbeit wird ohne R\"uckgabe der Schl\"ussel nicht
       entgegengenommen!}
    \fi
  \fi
  \vspace{2em}
  \global\let\@intdate\@empty
  \global\let\dateprefix\relax
  \global\let\dateprefixstring\@empty}
\endinput
%%

