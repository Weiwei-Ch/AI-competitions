
# coding: utf-8

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score

def trainer(model, df):
    train_x, val_x, train_y, val_y = train_test_split(df.drop(['id','fraud'], axis=1), df['fraud'], test_size=0.1, random_state=2021)
    print(train_x.shape, val_x.shape, train_y.shape, val_y.shape)
    clf = model.fit(train_x, train_y)
    pred_y = clf.predict(val_x)
    score = average_precision_score(val_y, pred_y)
    
    return clf, score

