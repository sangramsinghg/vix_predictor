
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="Images/logo_transparent.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">VIX Predictor</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#Presentation">Presentation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project : VIX PREDICTOR


### Team: Paola Carvajal, Sangram Singh, Ahmed Mohamed, Doreen Ngo

The VIX index is a forward indicator of the expected volatility of the S&P500. It moves rapidly and has continuous daily changes. It is called the "fear index". Our group applied Machine Learning and Time Series analysis to find a solution to predicting the VIX.

Through different techniques and models (AdaBoost, Neural Network, technical analysis, Facebook Prophet, Garch) we found three distinct models with more than 50% accuracy. These distinct models, techniques (PCA, Random Oversampler, Standard Scaler, Feature Selection, time series analysis, etc.) and strategies can be used to cater to wide variety of fintech customers. We use yfinance apis, google trends, economic and financial indicators to create features used in the Machine Learning models.

Our ML Model Architecture is: 

<img src="Images/model_architecture.png" alt="Logo" width="600" height="300">

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [JupyterLabs](https://jupyter.org)
* [adaBoost Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
* [SkLearn](https://scikit-learn.org/stable/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Facebook Prophet](https://facebook.github.io/prophet/)
* [Garch_Model](https://arch.readthedocs.io/en/latest/univariate/generated/arch.univariate.base.ARCHModel.html)


<!-- GETTING STARTED -->
## Getting Started

Below are examples of the necessary imports to run the code

 ```sh
  import pandas as pd
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder, MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import datetime
import numpy as np
import yfinance as yf
from datetime import datetime
from pandas.tseries.offsets import DateOffset
import hvplot
import hvplot.pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from vix_functions import garch_fit_and_predict, correlation_filter, retrieve_yahoo_close, retrieve_yahoo_volume
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
  ```

### Prerequisites /Installation

***To load all the necessary tools and files, please refer to the requirements.txt file

1) cd to the directory where requirements.txt is located.
2) activate your virtualenv.
3) run: pip install -r requirements.txt in your shell.

### Model files

1) vix_adaboost_model.ipynb
2) vix_predictor_finta.ipynb
3) vix_predictor_prophet.ipynb
4) vix_neural_neural_network_model.ipynb

<!-- USAGE EXAMPLES -->
## Usage

Below are images and examples of the model implementation to find the accuracy. 

### AdaBoost model: 

We are able to achieve 58% accuracy with the final AdaBoost Model. We plan to use this model for our high end hedge fund customers. This model has showen a ROI of 250x

<img src="Images/ClassificationReportAdaboost.png" alt="Logo" width="500" height="200">

We can see that our model is predicting very less negative returns as compared to the actual negative volatility.

<img src="https://github.com/sangramsinghg/vix_predictor/blob/main/Images/Good_and_bad_predictions_contrast.png" alt="Logo" width="600" height="300">

We get 22 features that contribute to the model. These are varied from Garch variables, treasuries, international exposure, global commodities, futures, squared returns, AAPL and the Friday effect.

<img src="Images/Features_importance.png" alt="Logo" width="1000" height="500">

We see that this model exhibits 250x ROI

<img src="Images/ProfitabilityPotencial.png" alt="Logo" width="600" height="300">

### AdaBoost Models using Technical Indicators:

The AdaBoost models that uses only Technical Indicators such as simple moving averages and bollinger bands. This model shows a ROI of 42X.

<img src="Images/adaboost_technical_indicator_model_roi.png" alt="Logo" width="600" height="300">

This models shows an accuracy of 55%

<img src="Images/adaboost_technical_indicator_classification_report.png" alt="Logo" width="400" height="300">

### Prophet:

Prophet analysis shows that volatilty dips on Friday and spikes on Monday. This shows a potential to make money by buying VIX on Friday and Selling it on Monday.

<img src="Images/prophet_time_series_analysis.png" alt="Logo" width="600" height="400">

The ROI based on this basic strategy is 28x.

<img src="Images/buy_friday_sell_monday_strategy.png" alt="Logo" width="600" height="300">


<!-- ROADMAP -->
## Roadmap

We are planning to release an MVP for our early adopters.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

* Paola Carvajal - [@Github](https://github.com/paocarvajal1912) - paola.antonieta@gmail.com
* Sangram Singh - [@Github](https://github.com/sangramsinghg) - sangramsinghg@yahoo.com
* Ahmed Mohamed - [@Github](https://github.com/Ahmed-Mahjoub) -  ahmedelkarar9@gmail.com
* Doreen Ngo - [@Github](https://github.com/ngomatterwhat) - doreen.sngo@gmail.com


<!-- Presentation -->
## Presentation
 
Below is a link to the presentation slide to our project:

[VIX_PITCHDECK](https://github.com/sangramsinghg/vix_predictor/blob/main/VIX%20PITCHDECK_2.pdf)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/scr
