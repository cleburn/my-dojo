* Hands-On ML: (notes)
CH 1 Overview
What is Machine Learning?
    "Machine Learning is the science (and art) of programming computers so they can learn from data."
    A computer is not smarter simply because new data is added (ex. Downloading all Wikipedia articles). A computer becomes smarter when, through experience, it can improve performance as it encounters new data.

Types of ML: Supervised vs Unsupervised:
    </Supervised> - is when the training set you feed to the algorithm includes the desired solutions called </labels> (typical for classification or regression)
    </Unsupervised> - is when the training date is </unlabeled> (clustering, anomaly detection, dimensionality reduction -> feature extraction)

What is a model? What is training?:
    </Model> - the type of structure on which the machine was built and trained. It is a mathematical representation that learns patterns from data to make predictions or decisions. (linear regression, decision trees, random forests, support vector machines (SVMs), neural networks, and k-nearest neighbors (KNN))
    </Training> - the process through which the model was given it's context and the way it learns to generalize/predict. It is the process of teaching a model to recognize patterns by exposing it to data and adjusting its internal parameters to minimize prediction errors.

Main challenges of ML:
    </Challenges> - obtaining high-quality data, avoiding overfitting or underfitting, ensuring model interpretability, managing computational complexity, and addressing bias and ethical concerns.

What's the difference between supervised and unsupervised learning?
    Whether or not the training data is labeled

What does 'training a model' actually mean?
    The process of using data to teach a model, evaluating its results, and adjusting its parameters to improve its results

Why do we split data into training and test sets?
    This allows us to use a controlled environment (data) to gauges the models efficiency. We split data into training and test sets to evaluate how well a model generalizes to new, unseen data rather than just memorizing the training examples.

CH 1 Recap:
    Supervised = labeled data (you know the answer, teach the model)
    Training = finding patterns by adjusting parameters
    Train/test split = prevents memorization, tests generalization
    Model is the structure, training is the learning process, data quality matters more than fancy algorithms.

---

CH 2 Overview
- Feature = input variable (like sqft, bedrooms)
- Target = what we're predicting (price)
- Training = model finds pattern in training data
- Testing = check if pattern works on unseen data

You want to predict house prices. You have these columns:

- `neighborhood`
- `square_feet`
- `bedrooms`
- `year_built`
- `price`

**Questions:**

1. Which column is your target? price
2. Which columns are your features? all the other columns
3. Why might neighborhood be useful for prediction? proximity to desirable locations - Neighborhood captures location value (downtown vs suburbs)
4. If you train on ALL your data, what problem might you face? inability to test and improve parameters before shipping - You won't know if model works on new/unseen houses (overfitting risk)

1. What's one ML concept that clicked today?
    the main difference between models and training methods (previously could not differentiate them just based on thier names)
2. What's one thing that still feels fuzzy? (This is expected!)
    Which libraries have which tools, and knowing what is the ideal tool for each stage of clearning and sorting the data
3. How does linear regression relate to the EDA you did in Month 1?
    starting to see LR as a mostly straightforward, supervised, instance based model of prediction that can be easily done in batch learning. So this is most of the EDA i did in month 1; collecting and sorting data, and predicting the best investment areas based on the target metrics

* Tuesday
Coding Practice:
Which column is your target? (What you're predicting)
    the target column is MedHouseVal, predicting the price based on this pricing column
Which columns are your features? (What you're using to predict)
    every other column

Understand Why We Split:
**The Problem:**

- If you train on ALL data, you can't test if the model works on NEW data
- Model might just memorize training examples (overfitting)

**The Solution:**

- Split data: 80% training, 20% testing
- Train model on 80%
- Test on the 20% it's never seen
- If it works on unseen data → model learned real patterns, not memorization

**Mental Model:**
Training data = study guide with answers
Test data = real exam (no answers shown during training)

**After First Model Training**
**Checkpoint Questions:**

1. What does the intercept represent?
    the model’s predicted output when all input features are zero — essentially the baseline value before any feature effects are applied
2. Which feature has the largest coefficient? (Biggest impact on price)
    AvgBedrooms has a substantially larger impact on the target than any other feature
3. What does a positive coefficient mean? Negative?
    A positive coefficient means that as the feature’s value increases, the predicted output (target value) also increases; a negative coefficient means that as the feature’s value increases, the predicted output decreases

**R² = how much of price variation the model explains. 1.0 = perfect, 0.0 = useless**

From </notebook:>
    Error Metrics:

    Mean Absolute Error (MAE): $0.5332 ($100k)
    In dollars: $53,320
    → On average, predictions are off by this amount

    Root Mean Squared Error (RMSE): $0.7456 ($100k)
    In dollars: $74,558
    → Penalizes large errors more than MAE
Looking at why one is more accurate than the other, in this case it is due to the very large outlier segment, to which the RMSE is more sensitive

notes from HOML book:
Both the RMSE and MAE are ways to measure the disatnce between two vectors: the vector of predictions and the vector of target values
The higher the norm index, the more it focuses on large values and neglects small ones. This is why the RMSE is more sensitive to outliers than the MAE. But when outliers are exponentially rare (like in a bell-shaped curve), the RMSE performs very well and is generally preferred

</RMSE> (Root Mean Squared Error) and </MAE> (Mean Absolute Error) are evaluation metrics used to measure how accurately a model’s predictions match the actual values

1. What surprised you about the model's predictions?
    How simple it was to walk the data through a few short steps, and to get easily visualized results.
2. Which feature had the biggest impact on price? Does that make intuitive sense?
    bedroom count had by far the biggest impact, which does make sense although I might have originally thought that total size or median income or location would have had equal or larger impact
3. Is your R² score better or worse than you expected? Why?
    Although it falls in the categories of being 'good,' I feel unsatisifed with the level of accuracy and am eager to learn how to improve
4. What's one thing you still don't fully understand?
    Still super fuzzy on which specific fucntions from their respective libraries to use; unclear on which loss/cost functions are ideal for each model ->

    Here are a few simple rules of thumb I researched:
	•	Regression tasks: Use MSE or MAE (MSE penalizes large errors more; MAE is more robust to outliers).
	•	Classification tasks: Use cross-entropy (log loss) for probabilistic outputs, or hinge loss for SVMs.
	•	Imbalanced data: Use weighted or focal loss to emphasize underrepresented classes.
	•	Custom goals: Choose or design a loss function that directly reflects the business or predictive objective (e.g., asymmetric loss for over/underestimation).

    </MSE> (Mean Squared Error) measures the average of the squared differences between predicted and actual values, while 
    </RMSE> (Root Mean Squared Error) is just the square root of MSE — putting the error back in the same units as the target variable.
    </SVMs> (Support Vector Machines) are supervised learning models that find the optimal boundary (or “hyperplane”) that best separates data points of different classes with the widest possible margin

## Wednesday - Day 3

**Residual = Actual Value - Predicted Value**

- Positive residual → Model predicted too low
- Negative residual → Model predicted too high
- Large residuals → Model is struggling with those examples
- Pattern in residuals → Model is missing something systematic

**Mental Model:** Residuals are the "leftover" error after your model does its best. If there's a pattern in the leftovers, your model missed something important

residual plot - pattern looks like there's definitely a systemic issue with the model.. rather than grouping tight along the 0 line, there is one solid line of dots as well as an unusual cluster of dots, neither of which are forming a clear pattern with the 0 line

</Claude>
## What GOOD vs BAD Residual Plots Look Like
**✅ GOOD (what you have):**
Random scatter, no pattern
Even spread above/below zero
Centered at zero

**❌ BAD patterns to watch for:**
1. CURVE - means you need polynomial features
2. VERTICAL BANDS - model only predicts certain values
3. SYSTEMATIC OVER/UNDER - bias in predictions
4. FAN SHAPE (yours is mild) - consider log transform


**Checkpoint Questions:**

1. Is training R² higher than test R²? (It usually should be slightly higher)
    yes
2. Is the difference large (>0.1) or small (<0.05)?
    Difference: 0.0368
3. What does this tell you about overfitting?
    Although the margins seem tolerable, it still makes me feel like the model is overly reliant on training data, and not yet super accurate with predicting new/unseen data. But according to the metrics notes that Claude shared, these differences actually indicate that the model generalizes well

Based on the scores, the model is well-balanced

**The Problem with Single Train/Test Split:**

- Your test score might be lucky (or unlucky)
- Different random split = different test score
- One score isn't enough to know true performance

**Cross-Validation Solution:**

1. Split data into 5 folds (chunks)
2. Train on 4 folds, test on 1 fold
3. Repeat 5 times (each fold gets to be test set once)
4. Average the 5 test scores → more reliable estimate

**Mental Model:** Instead of one exam, you take 5 different exams and average your grade. More reliable than one test.

**Where is your model on the bias/variance spectrum?**
    of the 7 features used, only 4 seem to have any notable impact. So perhaps there is a variance issue (overfitting), where we might achieve more accurate targets by removing some of the less meaningful features

## 📝 Reflection Questions:

1. What does your residual plot tell you about your model's weaknesses?
    model has difficulty with the higher priced outliers
2. Is your model overfitting, underfitting, or well-balanced? How do you know?
    Claude describes it as well-balanced.. but to me, a R^2 of .63 feels like possible overfitting due to unimpactful features. Still trying to get a clear feel and intuition here, so as i am not sure, i am allowing the exposure and the explanations from Claude to sink in and become a more firm grasp on the concept
3. Did cross-validation give you more or less confidence in your model? Why?
    CV kind of confirmed my suspicions that the model isn't generalizing as well as it could, since each fold had a fairly differnt result
4. Which feature surprised you most in terms of importance?
    I would have expected location or median income to be a bigger price indicator than avg bedrooms
5. What would you try next to improve model performance?
    Possible trimming the far-right ouliers, or removing the low-impact features

## Wednesday recap
CV Score Deep Dive - What I Learned:
My CV Results:

Mean R²: 0.5530
Std Dev: 0.0617 (moderate variation)
Range: 0.4682 to 0.6605

Key Insight: My gut was right to flag the variation, but wrong about the cause.
Not overfitting (train-test gap = 0.0368 proves this)
But: Model isn't perfectly robust (CV std > 0.05 shows performance varies by data sample)
What This Actually Means:

Some folds have easier/harder examples to predict
Fold 2 (0.47) struggled, Fold 5 (0.66) excelled
Signal that feature engineering will help stabilize performance
Baseline is solid, but there's room to capture patterns better

My Question 5 Ideas Were On Track:

✅ Trimming far-right outliers → Will reduce CV variance
✅ Removing low-impact features → Might help, but feature engineering to ADD better features is more powerful
Tomorrow: Feature engineering + polynomial features + regularization will address this

Takeaway: Trust the numbers over feelings, but also trust when something feels off—then investigate with data. My instinct to dig deeper was correct. The diagnosis just needed refinement.


# Thursday
