# IBM-Eval
Evaluation of hyperparameters in IBM federated Learning

## Aliases (Replace $PWD with the output of pwd)
alias fl_agg='python -m ibmfl.aggregator.aggregator $PWD/federated-learning-lib/examples/configs/iter_avg/keras/config_agg.yml'
alias fl_party0='python -m ibmfl.party.party $PWD/federated-learning-lib/examples/configs/iter_avg/keras/config_party0.yml'
alias fl_party1='python -m ibmfl.party.party $PWD/federated-learning-lib/examples/configs/iter_avg/keras/config_party1.yml'

## Pull the Federated Learning Repository
```
git clone https://github.com/Pauadins/Federated-Learning.git
```

## Navigate to the federated-learning-lib folder
```
cd ./federated-learning-lib
```

## Pull the IBM-Eval Repository
```
git clone https://github.com/Pauadins/IBM-Eval.git
```

## Copy the bash scripts to the federated-learning-lib directory
```
cp ./IBM-Eval/*.sh .
```

## Start Federation
Create three tmux sessions with the following commands:
```
tmux new-session -d -s Aggregator -n "Aggregator" -c "$PWD"
tmux new-session -d -s Party0 -n "Party0" -c "$PWD"
tmux new-session -d -s Party1 -n "Party1" -c "$PWD"
```

## Initialize the conda environment in each session
```
tmux send-keys -t Aggregator "conda activate fl_sim" C-m
tmux send-keys -t Party0 "conda activate fl_sim" C-m
tmux send-keys -t Party1 "conda activate fl_sim" C-m
```

## Exit the tmux sessions
```
tmux detach -s Aggregator
tmux detach -s Party0
tmux detach -s Party1
```

## Run the hyperparameter sweep
```
bash hyperparam.sh
```