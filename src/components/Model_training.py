from transformers import TrainingArguments,Trainer,DataCollatorForSeq2Seq,AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset,load_from_disk
import torch
from src.entity.config_entity import ModelTrainingConfig
from src.config.configuration import ConfigurationManager
import os
import sys


class ModelTrainer:

    def __init__(self,config=ModelTrainingConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model_pegasus)

        data_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args =  TrainingArguments(
            output_dir=self.config.root_dir,num_train_epochs=self.config.num_train_epoch,warmup_steps=self.config.warmp_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,eval_steps=self.config.eval_steps,save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            train_dataset=data_samsum_pt['train'],
            eval_dataset=data_samsum_pt['validation']
        )

        trainer.train()
        #save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        #save tokenizer

        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
        


