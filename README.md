# nasa_imagery_autotests
Autotests for nasa /planetary/earth/imagery api endpoint

First before start install pip -r requirements.txt


To run smoke tests use 'behave --tags=smoke'
To run extended parametric tests use 'behave --tags=extended'
To run negative parametric tests use 'behave --tags=negative'

To run all tests use 'behave --tags=main_batch'


To run tests with allure report generating use

behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features

and serve results

allure serve allure_result_folder