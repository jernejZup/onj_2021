
from models.models import BERT
from models.tools.data_loader import BERT_dataloader


def main(SEQ_LENGTH=128):
    path=['dataset/slo_tviti.csv','dataset/tviti_neobdelani.csv']
    tcn=['tweet','tweet']
    lcn=['is_offensive','bool_offensive']


    bert_dataloader=BERT_dataloader(seq_length=SEQ_LENGTH,batch_size=32)
    bert_dataloader.load_data(path,text_column_name=tcn,label_column_name=lcn,val_df=1)
    train,val=bert_dataloader.get_data()
    bert=BERT(seq_length=SEQ_LENGTH)
    model=bert.get_model()
    callbacks=bert.get_callbacks('weights','slovenski_tviti')
    model.fit(train,validation_data=val,epochs=5,callbacks=callbacks)




if __name__ == '__main__':
    main()

