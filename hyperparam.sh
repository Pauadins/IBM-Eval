# Iterate through hyperparameters and call run_federation.sh
# Hyperparameters being tested: max_timeout, rounds, termination_accuracy

# create log file if it doesn't exist
if [ ! -f "log.csv" ]; then
	touch log.csv
	# Header for log file (Party, Loss, Accuracy, Precision)
	echo "Party, Loss, Accuracy, Precision" >> log.csv
fi


# max_timeout ranges from 0 to 200
for max_timeout in {0..200..10}
do
	# rounds ranges from 1 to 5
	for rounds in {1..5}
	do
		# termination_accuracy ranges from 0.90 to 0.99
		for termination_accuracy in {0.90..0.99..0.01}
		do
			# Modify the config file with the hyperparameters
			sed -i "s/^ *max_timeout: .*/  max_timeout: $max_timeout/" config.yaml
			sed -i "s/^ *rounds: .*/  rounds: $rounds/" config.yaml
			sed -i "s/^ *termination_accuracy: .*/  termination_accuracy: $termination_accuracy/" config.yaml

			# Run the federation
			./run_federation.sh
			
			# 
			# Wait for training to complete in both sessions
			tmux wait-for Party0
			tmux wait-for Party1

			# pull loss, accuracy, and precision values (floating point) from console output of each tmux session and append to log.csv
			output=$(tmux capture-pane -p -t Party0)
			loss=$(echo "$output" | awk -F "'loss': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			accuracy=$(echo "$output" | awk -F "'acc': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			precision=$(echo "$output" | awk -F "'precision weighted': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			# echo "Party0, loss: $loss, accuracy: $accuracy, precision: $precision" >> log.csv
			echo "0, $loss, $accuracy, $precision" >> log.csv
			
			output=$(tmux capture-pane -p -t Party1)
			loss=$(echo "$output" | awk -F "'loss': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			accuracy=$(echo "$output" | awk -F "'acc': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			precision=$(echo "$output" | awk -F "'precision weighted': " 'NF>1{print $2}' | awk -F "," 'NF>1{print $1}' | head -1)
			# echo "Party1, loss: $loss, accuracy: $accuracy, precision: $precision" >> log.csv
			echo "1, $loss, $accuracy, $precision" >> log.csv
		done
	done
done
