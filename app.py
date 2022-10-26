{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acb7aba0",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-10-26T16:54:18.695635Z",
     "start_time": "2022-10-26T16:54:15.316647Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-10-26 12:54:16.225222: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F AVX512_VNNI FMA\n",
      "To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import gpt_2_simple as gpt2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e8b98f24",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-10-26T16:55:05.415339Z",
     "start_time": "2022-10-26T16:55:05.411119Z"
    }
   },
   "outputs": [],
   "source": [
    "app = Flask(__name__) \n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template('home.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d3765699",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-10-26T17:31:10.953728Z",
     "start_time": "2022-10-26T16:55:07.298769Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [26/Oct/2022 12:55:10] \"GET / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    import gpt_2_simple as gpt2\n",
    "    sess = gpt2.start_tf_sess()\n",
    "    gpt2.load_gpt2(sess, run_name='run1')\n",
    "    text = gpt2.generate(sess, run_name='run1',\n",
    "              temperature=0.7,\n",
    "              top_k=40,\n",
    "              nsamples=1,\n",
    "              batch_size=25,\n",
    "              prefix=\"<|startoftext|>[WP] What should I do if I feel depressed?\",\n",
    "              truncate=\"<|endoftext|>\",\n",
    "              include_prefix=False,\n",
    "              sample_delim='')\n",
    "                #return_as_list=True)[0]\n",
    "    return render_template('home.html', prediction_text=text)\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True,use_reloader=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
