# The Research Table

A card-table activity builder for teaching research writing.

Teachers set up two activities, preview them, and download a single self-contained HTML file to share with students through a learning platform (Brightspace, Canvas, Moodle), Teams, or email. The file works offline.

- **Activity 1 · Write an Intro.** Teams draw an education level card and a topic card, then write the four parts of a research introduction (hook, background, problem, purpose), using the teacher's example sentences as models.
- **Activity 2 · Guess the Research Questions.** Teams pick an article, read its abstract and the passage that leads up to its research questions, write their guess, and flip a card to reveal the real questions.

Both activities end with a "payout ticket" image that students can download or print to submit.

Live site: https://researchtable.collegetowns.org

## Privacy

Everything runs in the browser. Nothing a teacher or student types is sent anywhere. The builder autosaves in the teacher's own browser (localStorage), and each student's writing stays in their own browser.

## Editing the app

`index.html` (the teacher builder) and `demo.html` (the default student activity) are generated. Edit the files in `src/` and then run:

```
python3 build.py
```

- `src/builder-src.html`: the teacher builder
- `src/student-src.html`: the student activity (the builder fills in `/*__CONFIG__*/`)
- `src/defaults.json`: the default title, decks and example sentences
- `src/starter-articles.json`: the four starter articles
- `src/icons.json`: the card symbols (24×24 SVG paths, also drawn on the ticket)

## Starter articles

New activities start with four starter articles taken from real open-access studies; teachers can remove them, add them back, edit them, or add their own. They are reproduced under each article's Creative Commons license, and the citation, link and license are shown to students with each article.

| Article | Source | License |
|---|---|---|
| Generative AI in higher education | Chan, C. K. Y., & Hu, W. (2023). Students' voices on generative AI: Perceptions, benefits, and challenges in higher education. *International Journal of Educational Technology in Higher Education, 20*, Article 43. https://doi.org/10.1186/s41239-023-00411-8 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Principal stress in Finland | Elomaa, M., Eskelä-Haapanen, S., Pakarinen, E., Halttunen, L., & Lerkkanen, M. K. (2023). Work-related stress of elementary school principals in Finland: Coping strategies and support. *Educational Management Administration & Leadership, 51*(4), 868–888. https://doi.org/10.1177/17411432211010317 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| After-school STEM clubs | Blanchard, M. R., Gutierrez, K. S., Swanson, K. J., & Collier, K. M. (2023). Why do students attend STEM clubs, what do they get out of it, and where are they heading? *Education Sciences, 13*(5), 480. https://doi.org/10.3390/educsci13050480 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| School gardens | Hellinger, F., Benkowitz, D., & Lindemann-Matthies, P. (2022). Do radishes and carrots grow in a bunch? Students' knowledge about the growth of food plants and their ideas of a school garden design. *Education Sciences, 12*(5), 299. https://doi.org/10.3390/educsci12050299 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Abstracts, lead-in passages and research questions are reproduced as published, except that the Chan & Hu lead-in was shortened (cuts are marked with … and noted under the article). Each lead-in is the passage immediately before the article's research questions; short card titles were added.

Only include material you have the right to share; everything entered is embedded in the downloaded file.
