import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.metrics import confusion_matrix

def training_plot(hist):
    loss = [hist.history['loss'],hist.history['val_loss']]
    acc = [hist.history['acc'],hist.history['val_acc']]
    
    fig, axes = plt.subplots(1,2,figsize = (15,3))
    for ax,val,name in zip(axes,(loss,acc),['loss','accuracy']):
        ax.plot(val[0], color='b', label="Training")
        ax.plot(val[1], color='r', label="Validation")
        ax.legend(loc='best')
        ax.set_xlabel('epoch')
        ax.set_ylabel('')
        ax.set_title(name)

def confusion_matrix_plot(y_true,y_pred,model_name):
    
    confusion_mtx = confusion_matrix(y_true,y_pred)
    confusion_mtx_normalized = confusion_mtx/confusion_mtx.sum(axis=1)

    plt.figure(figsize=(8,4))
    sns.heatmap(confusion_mtx,annot=True,cmap='coolwarm',fmt='d')
    plt.title('confusion matrix of '+ model_name)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
    
    plt.figure(figsize=(8,4))
    sns.heatmap(confusion_mtx_normalized,annot=True,cmap='coolwarm')
    plt.title('Normalized confusion matrix of '+ model_name)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
    
    plt.figure()
    plt.title('Correct prediction rate (%) of ' + model_name)
    sns.barplot(np.arange(len(np.unique(y_true))),np.diag(confusion_mtx_normalized)*100)
    plt.xlabel('Classes')