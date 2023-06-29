The suite of tests for the website https://hb-eta.stage.sirenltd.dev/siding  
To run tests use the command:  
1. All tests with report: 'pytest --html=report.html test_siren_website.py'  
2. Main flow: 'pytest test_siren_website.py::def test_siren_website'  
3. Unsupported Zip code: 'pytest test_siren_website.py::test_zip_code_unsupported'  
4. Wrong siding square area: 'pytest test_siren_website.py::test_wrong_siding_area_value'
5. The 3+ stories message: 'pytest test_siren_website.py::test_stories_warning'

Main flow:  
-- zip code 09090  
-- answer the questions on the form  
-- enter the first and last name  
-- enter an email  
-- enter the phone number  
-- (if necessary) confirm the phone number  
-- get a "thank you" page.  
  
Prerequisite:  
Python3  
pip install -U pytest  
pip install pytest-selenium