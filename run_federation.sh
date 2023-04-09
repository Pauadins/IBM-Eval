#!/bin/bash

# Create a new TMUX session named 'Aggregator' with one pane
#tmux new-session -d -s Aggregator -n "Aggregator" -c "$PWD"
#    conda init && sleep 5 && conda activate fl_sim && fl_agg
tmux send-keys -t Aggregator:0 "fl_agg" Enter
# Wait until initialization completes in the pane
while [[ $(tmux capture-pane -p -t Aggregator:0) != *"Aggregator initialization"* ]]; do
    sleep 1
done

# Start the pane and wait until 'Running on' appears
tmux send-keys -t Aggregator:0 "START" Enter
while [[ $(tmux capture-pane -p -t Aggregator:0) != *"Running on"* ]]; do
    sleep 1
done

# Create two new TMUX sessions named 'Party0' and 'Party1' with one pane each
#tmux new-session -d -s Party0 -n "Party0" -c "$PWD"
#    conda init && sleep 5 && conda activate fl_sim && fl_party0
tmux send-keys -t Party0:0 "fl_party0" Enter
#tmux new-session -d -s Party1 -n "Party1" -c "$PWD"
#    conda init && sleep 5 && conda activate fl_sim && fl_party1
tmux send-keys -t Party1:0 "fl_party1" Enter
# Wait until initialization completes in each pane
while [[ $(tmux capture-pane -p -t Party0:0) != *"Party initialization successful"* ]]; do
    sleep 1
done
while [[ $(tmux capture-pane -p -t Party1:0) != *"Party initialization successful"* ]]; do
    sleep 1
done

# Start each pane in 'Party0' and 'Party1' sessions and wait until 'Running on' appears
tmux send-keys -t Party0:0 "START" Enter
while [[ $(tmux capture-pane -p -t Party0:0) != *"Running on"* ]]; do
    sleep 1
done

tmux send-keys -t Party1:0 "START" Enter
while [[ $(tmux capture-pane -p -t Party1:0) != *"Running on"* ]]; do
    sleep 1
done

# Send 'REGISTER' in panes of 'Party0' and 'Party1' sessions and wait until 'Registration Successful'
tmux send-keys -t Party0:0 "REGISTER" Enter
while [[ $(tmux capture-pane -p -t Party0:0) != *"Registration Successful"* ]]; do
    sleep 1
done

tmux send-keys -t Party1:0 "REGISTER" Enter
while [[ $(tmux capture-pane -p -t Party1:0) != *"Registration Successful"* ]]; do
    sleep 1
done

# Send 'TRAIN' in pane of 'Aggregator' session and wait until 'Finished Global Training'
tmux send-keys -t Aggregator:0 "TRAIN" Enter
while [[ $(tmux capture-pane -p -t Aggregator:0) != *"Finished Global Training"* ]]; do
    sleep 1
done

# Send 'EVAL' in pane of 'Aggregator' session and wait until 'Finished eval requests'
tmux send-keys -t Aggregator:0 "EVAL" Enter
while [[ $(tmux capture-pane -p -t Aggregator:0) != *"Finished eval requests"* ]]; do
    sleep 1
done

# Send 'STOP' in all 3 panes
tmux send-keys -t Aggregator:0 'STOP' Enter
tmux send-keys -t Party0:0 'STOP' Enter
tmux send-keys -t Party1:1 'STOP' Enter