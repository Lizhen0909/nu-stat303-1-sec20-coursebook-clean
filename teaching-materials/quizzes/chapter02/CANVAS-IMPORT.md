# Import the Chapter 2 quiz into Canvas

Import `chapter02-canvas-quiz.zip` directly; do not unzip it.

The package targets Canvas Classic Quizzes using QTI 1.2 with Canvas metadata. It includes four single-answer MCQs (1 point each), their encoded correct choices, and one file-upload question (16 points). Total: 20 points. The quiz description and upload prompt link to Chapter 2 as the single source of activity instructions. No visible correct-answer markers are included in student question text.

## Classic Quizzes

1. In the Canvas course, open **Settings → Import Course Content**.
2. Choose **QTI .zip file** and select `chapter02-canvas-quiz.zip`.
3. For a Classic Quiz import, leave conversion to New Quizzes unchecked, if shown. Leave overwrite-with-matching-IDs unchecked for an initial import.
4. Start the import (the button may say **Import** or **Add to Import Queue**).
5. After completion, open **Quizzes** and locate **Chapter 2 Quiz: Your Python Environment and Project Files**.
6. Preview it: confirm four MCQs, the final file-upload control, a 20-point total, and working Chapter 2 links. In the editor, confirm the correct choices match D, A, B, D in the unshuffled instructor draft.
7. Set your dates, attempts, and feedback visibility, then publish when ready. The package requests an unpublished quiz with correct-answer display disabled; review the imported settings before release.

The upload prompt requests `activity02.html`. The package does not enforce a filename or file-extension restriction. Grade the upload manually using `chapter02-quiz-instructor.md`; the rubric is not attached automatically.

## If your course uses New Quizzes

Canvas documents a separate route: create a New Quiz, open its Build page, and use its internal Import command to select the QTI ZIP. Some institutions also enable conversion during course content import. This package uses Canvas Classic's file-upload metadata; its conversion to New Quizzes has not been tested. Preview all five imported questions, especially the upload control, before using it with students.

## Validation

The ZIP/XML structure, resource references, four answer keys, file-upload metadata, total points, and absence of visible answer markers were checked locally. The package has not been imported into your Canvas account, so successful end-to-end import is not yet verified.

Official instructions: https://community.instructure.com/en/kb/articles/660996-how-do-i-import-quizzes-from-qti-packages

The generator follows Canvas's public QTI exporter:
https://github.com/instructure/canvas-lms/blob/master/lib/cc/qti/qti_items.rb
https://github.com/instructure/canvas-lms/blob/master/lib/cc/qti/qti_generator.rb

To rebuild after editing the Markdown quiz draft, run `python teaching-materials/quizzes/chapter02/build_chapter02_qti.py` from the repository root.
