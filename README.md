# IBM-Eval
Evaluation of hyperparameters in IBM federated Learning

# Start Federation
Create three tmux sessions with the following commands:
```
tmux new-session -d -s Aggregator -n "Aggregator" -c "$PWD"
tmux new-session -d -s Party0 -n "Party0" -c "$PWD"
tmux new-session -d -s Party1 -n "Party1" -c "$PWD"
```

Initialize the conda environment in each session
```
conda activate fl_sim
```
