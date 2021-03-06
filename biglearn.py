'''BigMl module for Data/Ia Dev Script -- Nicolas Autexier -- contact = nicolas.atx@gmx.fr '''

from pandas import read_csv
import pandas
import os
import matplotlib.pyplot as plt
import sys
from bigml.api import BigML
from bigml.model import Model
from graph import rViz
from sec import secureLog as SL

def initproject():
    api = BigML(f'{SL.bigUseur}', f'{SL.bigApiKey}', project=f'{SL.pjt_id}')
    return api
api = initproject()

################ Prediction sur fichier train/validation ###################  

def predmeth1(file,fileTest,splitTrain,splitTest,mod,objectifField,export) :

    modvar = modelOperate(mod,file,objectifField) 
    api.ok(modvar)
    print("predict-lancée")    

    batch_prediction = api.create_batch_prediction(modvar, fileTest,{"all_fields": True,"probabilities": True, "prediction_name" : "pred"})
    api.ok(batch_prediction)

    evaluation = api.create_evaluation(modvar,fileTest) 
    api.ok(evaluation)  
    # api.pprint(evaluation['object']['result'])
    # api.pprint(evaluation['object']['result']['Ensemble training']['accuracy'])
    # api.pprint(evaluation['object']['result']['Ensemble training']['average_area_under_roc_curve'])
    
    api.download_batch_prediction(batch_prediction,filename=f"Pred_Files/{export}")

    print("prediction ok")

################ Prediction sur fichier prod ###################

def predmeth1Kagg (modid,modTypes,fileTest,export) :

    source_test = api.create_source(fileTest)
    api.ok

    test_testdataset = api.create_dataset(source_test)
    api.ok

    print("fichier ok")

    modvar = getModel(modid,modTypes)
    api.ok(modvar)
    print("predict-lancée")
    
    batch_prediction = api.create_batch_prediction(modvar, test_testdataset,{"all_fields" : True,"probabilities" : True, "prediction_name" : "pred"})
    api.ok(batch_prediction)

    # evaluation = api.create_evaluation(modvar,fileTest)
    # api.ok(evaluation) 
    api.download_batch_prediction(batch_prediction,filename=f"Pred_Files/{export}")

    print("prediction ok")
    
########### Gestion du script #####################

def modelOperate(mod,train_dataset,objectifField) :
    if mod == 'ensemble':
        modvar = api.create_ensemble(train_dataset, {"objective_field": f"{objectifField}", "name": "ensemble"}) 
    elif mod == 'model':
        modvar = api.create_model(train_dataset, {"objective_field": f"{objectifField}", "name": "model"})
    elif mod == 'deepnet': 
        modvar = api.create_deepnet(train_dataset, {"objective_field": f"{objectifField}", "name": "deepnet"}) 
    elif mod == 'linear': 
        modvar = api.create_linear_regression(train_dataset, {"objective_field": f"{objectifField}" ,"name": "linear"})      
    else :
        print("mod non pris en charge ! programme terminé !!")
        exit()
    return modvar    

def getModel(model_One,var_mod) :
    if var_mod == 'ensemble':
        setmod = api.get_ensemble(f"{model_One}") 
    elif var_mod == 'model':
        setmod = api.get_model(f"{model_One}")
    elif var_mod == 'deepnet': 
        setmod = api.get_deepnet(f"{model_One}") 
    elif var_mod == 'linear': 
        setmod = api.get_linear_regression(f"{model_One}")      
    else :
        print("mod non pris en charge ! programme terminé !!")
        exit()
    return setmod  

########### creation de prediction #####################
 
class createNewPred() :

    @staticmethod
    def newDataSet():

        file = str(input("Nom du fichier full train : "))
        splitTrain = float(input("valeur split train : "))
        splitTest = float(1 - splitTrain)
        mod = str(input("Model selectioné : "))
        objectifField = str(input("Nom du champs objectif : "))
        export = str(input("Nom du fichier exporté : "))

        source = api.create_source(f"{file}")
        api.ok
        origin_dataset = api.create_dataset(source)
        api.ok
        train_dataset = api.create_dataset(origin_dataset, {"name": "VarTraining", "sample_rate": splitTrain})
        test_dataset = api.create_dataset(origin_dataset, {"name": "VarTest", "sample_rate": splitTest})
        api.ok
        file = train_dataset
        fileTest = test_dataset
        print("split ok")

        predmeth1(file,fileTest,splitTrain,splitTest,mod,objectifField,export)

    @staticmethod
    def loaddDataSet() :

        c_condition = bool(input("Appliquer nouveau split (true or false) ?"))

        if c_condition :
            s_source = str(input("train full dataset/id : "))
            n_source = api.get_dataset(f"{s_source}")
            splitTrain = float(input("valeur split train : "))
            splitTest = float(1-splitTrain)
            train_dataset = api.create_dataset(n_source, {"name": "VarTraining", "sample_rate": splitTrain})
            test_dataset = api.create_dataset(n_source, {"name": "VarTest", "sample_rate": splitTest})
            mod = str(input("Model selectioné : "))
            objectifField = str(input("Nom du champs objectif : "))
            export = str(input("Nom du fichier exporté : "))
            file = train_dataset
            fileTest = test_dataset
            print("dataset load ok") 
        else :    
            n_dataset = str(input("train dataset/id : "))
            train_dataset = api.get_dataset(f"{n_dataset}")
            t_dataset = str(input("test dataset/id : "))
            test_dataset = api.get_dataset(f"{t_dataset}")
            mod = str(input("Model selectioné : "))
            objectifField = str(input("Nom du champs objectif : "))
            export = str(input("Nom du fichier exporté : "))
            file = train_dataset
            fileTest = test_dataset
            splitTrain = 0
            splitTest = 0
            print("dataset load ok") 

        predmeth1(file,fileTest,splitTrain,splitTest,mod,objectifField,export)

    @staticmethod
    def predOnProdSet() :
        fileTest = str(input("Nom du fichier full Prod : "))
        modid = str(input("Modèle id : "))
        modTypes = str(input("Types de Modèle  : "))
        export = str(input("Nom du fichier exporté : "))

        predmeth1Kagg(modid,modTypes,fileTest,export)

##################### Meth pour split les full test en dev test et test_test(genre kaggle) ##############################

# test_full = api.create_dataset(origin_dataset, {"name": "test_full"})
# rest = 1-splitTrain
# sep= rest/2
# print("reste pour test : ",sep)
# test_test = api.create_dataset(test_full, {"name": "dev_test", "sample_rate": sep})
# test_test = api.create_dataset(test_full, {"name": "test_final", "sample_rate": sep}) 


########### Analyse BigMl #####################
class analyserML() :
    
    @staticmethod
    def compar2model():
    ###### Comparaison AUC/Ammont of data entre 2 models #########
        ###### variable d'environement #########
        load_set_train = str(input("Id du fichier train : "))
        load_set_test = str(input("Id du fichier test : "))
        objectifField = str(input("Nom du champs objectif : "))
        model_One = str(input("model 1 : "))
        model_two = str(input("model 2 : "))
        var = 0.1
        tablex = []
        tabley = []
        tabley2 = []
        ###### Routine Big ML #########
        for i in range(0,10):
            print("Step : ",i)
        
            origin_dataset = api.get_dataset(f"{load_set_train}")
            api.ok
            train_dataset = api.create_dataset(origin_dataset, {"name": "AmountData2", "sample_rate": var})
            api.ok
            fileTest = api.get_dataset(f"{load_set_test}")
            api.ok

            ###### Appel de la fonction create_"" #########
            modvar = modelOperate(model_One,train_dataset,objectifField)

            evaluation = api.create_evaluation(modvar,fileTest)
            api.ok(evaluation)
            auc = evaluation['object']['result']['model']['average_area_under_roc_curve']
            print(f"auc {model_One} : ", auc, "avec un split : ", var)

            tablex.append(var)
            tabley.append(auc)

            ###### Appel de la fonction create_"" #########
            modvar = modelOperate(model_two,train_dataset,objectifField)

            evaluation = api.create_evaluation(modvar,fileTest)
            api.ok(evaluation)
            auc = evaluation['object']['result']['model']['average_area_under_roc_curve']
            print(f"auc {model_two} : ", auc, "avec un split : ", var)

            tabley2.append(auc)

            var += 0.1
            var = round(var,2)
        ###### Appel du module graphique #########
        rViz.graph_double(tablex,tabley,tabley2)
        rViz.extraction()        

    @staticmethod        
    def summuary() : 
    ###### Methode publié sur discord par Christophe #########
        model_One = str(input("model ID : "))
        var_mod = str(input("model name : "))
        model = getModel(model_One,var_mod)
        importances = model['object']['importance']
        importances_named = dict()
        for column, importance in importances.items():
            column_name = model['object'][f'{var_mod}']['fields'][column]['name']
            importances_named[column_name] = [importance * 100]
        df = pandas.DataFrame.from_dict(importances_named, orient='index')
        df = df.sort_values(0, ascending=False)
        df.plot(kind='bar', color='green', legend=False)
        plt.draw()
        plt.show()

class singlePredProd() :

    @staticmethod
    def singlePred(model_id,model_types,array_imput):

        mod = model_types
        model = getModel(model_id,mod)
        api.ok(model)

        input_data = {"title": array_imput[0], "synopsis": array_imput[1], "rating": array_imput[2], "genre": array_imput[3], "duration": array_imput[4],
        "release_date": array_imput[5], "director": array_imput[6],"people": array_imput[7], "produceur": array_imput[8],"country": array_imput[9], 
        "writer": array_imput[10]}

        prediction = api.create_prediction(model, input_data)

        api.ok(prediction)
        value_pred = prediction["object"]["output"]
        return value_pred
        #print("prediction : %s, confidence: %s %",(prediction["object"]["output"],prediction["object"]["confidence"] ))    

    @staticmethod
    def localSinglePred(model,vals1,vals2):

        input_data2 = {"features1": vals1, "features2": vals2}
        local_model = Model(model)# model Id
        local_model.predict(input_data2) # add_confidence=True)